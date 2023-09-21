import sys
import openai
import os
import asyncio


openai.api_key = os.getenv("OPENAI_API_KEY")


async def create_training_file(filename: str):
    file_create_output = await openai.File.acreate(
        file=open(filename, "rb"), purpose="fine-tune"
    )
    print(f"Created training file: {file_create_output}")
    return file_create_output


async def start_finetune_job(training_file: str):
    ft_job = await openai.FineTuningJob.acreate(
        training_file=training_file, model="gpt-3.5-turbo"
    )
    print(f"Created fine tuning job: {ft_job}")
    return ft_job


async def check_file_status(file_id: str):
    response = await openai.File.aretrieve(file_id)
    print(response)
    return response


async def train(filename: str):
    file_create_output = await create_training_file(filename=filename)
    await start_finetune_job(training_file=file_create_output["id"])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File Handling and Training Script")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create a subparser for the 'create_file' command
    create_file_parser = subparsers.add_parser("create_file", help="Create a file")
    create_file_parser.add_argument(
        "path_to_file", help="Path to the file to be created"
    )

    # Create a subparser for the 'file_status' command
    create_file_parser = subparsers.add_parser("file_status", help="Create a file")
    create_file_parser.add_argument("file_id", help="Id of the uploaded file")

    # Create a subparser for the 'train' command
    train_parser = subparsers.add_parser(
        "fine_tune", help="Fine tune using an uploaded file"
    )
    train_parser.add_argument(
        "filename", help="Name of the uploaded file for fine tuning"
    )

    args = parser.parse_args()

    match args.command:
        case "create_file":
            asyncio.run(create_training_file(filename=args.path_to_file))
        case "file_status":
            asyncio.run(check_file_status(file_id=args.file_id))
        case "fine_tune":
            asyncio.run(start_finetune_job(training_file=args.filename))
        case _:
            parser.print_help()
            sys.exit(1)
