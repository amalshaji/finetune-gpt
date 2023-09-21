# Fine tune gpt-3.5

## To run

- Set `OPENAI_API_KEY` in environment.
- run `python no_fine_tune.py` to run non fine tuned version
- run `python nofine_tune.py` to run fine tuned version

## To train

- Use the train.py script

```shell
usage: train.py [-h] {create_file,file_status,fine_tune} ...

File Handling and Training Script

positional arguments:
  {create_file,file_status,fine_tune}
                        Available commands
    create_file         Create a file
    file_status         Create a file
    fine_tune           Fine tune using an uploaded file

options:
  -h, --help            show this help message and exit
```
