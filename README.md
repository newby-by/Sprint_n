<img src="./resource/python-logo-only.svg" width="20" height="20"><img src="./resource/1280px-Selenium_Logo.png" width="20" height="20"><img src="./resource/images.jfif" width="20" height="20"> 

# The test bicycle for Yandex's Route app

[See here the site](https://qa-routes.education-services.ru/)

We made x-broswer tests with chrome, firefox and etc. 
How to start with Docker or local, see below, though.

## Acknowledgements

The Praktikum team

[Artem Yaroshenko whom power is unlimited.](https://github.com/eroshenkoam)

My Tomcat that got me up early.
Your 4 a.m. song was so cool.(RIP)

## Requirements
    python~=3.13.13
    allure-pytest
    pytest
    selenium==3.141.0

*Note:* For local test run we use `webdriver-manager`: Chrome, Gecko and etc.

*Note:* For remote test run we use `selenoid`.

## How to start local 
1. Create venv
```bash
py -3.13 -m venv venv
```
2. Activate venv
```bash
source venv/Scripts/activate
```
3. Install requirements 
```bash
pip install -r requirements.txt
```
4. Run tests
```bash
pytest
```
*Note:* For more details use key `-vv`.
```bash
pytest -vv
```
*Note:* For creating allure reports add `--alluredir=allure-results`.

*Note:* [How to start allure](https://allurereport.org/docs/how-it-works/)
