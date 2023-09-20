# SHLOK-AI
## SHLOK-AI FEATURE PREVIEW
[![[PREVIEW] Shlok-AI: Experience the richness of Vedic literature and Indian Civilization with AI](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D7SNpiyXNdIk)](https://www.youtube.com/watch?v=7SNpiyXNdIk)

## SHLOK-AI FEATURE PREVIEW [EXTENDED]
[![[EXTENDED] Shlok-AI: Experience the richness of Vedic literature and Indian civilization with AI](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DU2lNVSMqiAA)](https://www.youtube.com/watch?v=U2lNVSMqiAA)

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

6. Ensure node and npm are installed in your environment

<!-- 7. Install required packages in the npm app
```bash
cd shlok-ai
npm install
``` -->

<!-- 8. Install required packages in the react app
```bash
cd shlok-ai

```  -->


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

## Start Shlok-AI
1. Execute Flask API script so the API Endpoints are made available
    - `python api.py`
2. From the home folder of the npm app,
    - `cd shlok-ai` 
    - `npm run start`

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

# Container deployment
Use docker compose to provision the microservices for shlok-ai API and shlok-ai UI. 

The below command will build the images as well as bring up both the containers:

```
docker-compose -f docker-compose-shlok-ai.yml up -d --build
```
