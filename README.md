# Shlok-ai
## Installation instructions
1. Clone the github repository
`git clone https://github.com/initd1/Shlok-AI.git`

## Environment Set-up

1. Install python-pip in your environment
2. Install virtualenv
`pip install virtualenv`
3. Create virtual environment
`virtualenv <environment-name>`
4. Activate virtual environment  
__Mac or Linux__
```bash
source <environment-name>/bin/activate
```
__Windows__
```bash
<environment-name>\Scripts\activate.bat
```

5. Install required packages in the virtual environment
```python
pip install -r requirements.txt
```

## Prerequisites
1. Ensure `config.ini` file is created under Config directory
2. Use `config.ini.template` file as a reference and fill the required details. 
3. Rename `config.ini.template` to `config.ini`
    
    Preview of `config.ini.template` file: 
    ```ini
    [OPENAI]
    OPENAI_API_KEY=
    MODEL=
    ```

## Testing

It is important that before you do anything you have the `requirements.txt` file
installed as it is required for the dependencies that are used in this project.

To install all dependencies listed in this file, run the following:

```bash
python -m pip install -r requirements.txt
```

To execute tests, please ensure that you have the `pytest` module installed.
The unittest module is used, however, this is native to python and does not have to be installed.
To run tests, please ensure that you are in the base directory, where `Tests` and `main.py` is visible.

To run tests with print output:
```bash
pytest -s 
```

To run tests without print output:
```bash
pytest
```
> **Warning** pytest will not run if python site-packages are not already in your global path!
