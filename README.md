# StreamZ
![GitHub](https://img.shields.io/github/license/vijay9908/StreamZ)
![GitHub last commit](https://img.shields.io/github/last-commit/vijay9908/StreamZ)

#### A video streaming platform made as a project for Software-Engineering in S6.

The following folder has the documentation prepared with all the SE steps followed in each phase. 

[Software requirement specification (SRS)](https://drive.google.com/file/d/1YKYFkZbOwhASNs7PFR4IRXAi8jgB87Ek/view?usp=sharing)

[Use-case Diagram](https://drive.google.com/file/d/1da8WVXbpyeQuUktQWfv9XL_ecZbr6zcD/view?usp=sharing)

[Class Diagram](https://drive.google.com/file/d/1Pl3BqF4xQJWwuWiEz-MMWPo4ORoD41AH/view?usp=sharing)

[Sequence Diagram](https://drive.google.com/file/d/1GfxSpwEDYJoEGMFc8veUghkbsj56okXT/view?usp=sharing)

[Test-plan](https://drive.google.com/file/d/16fObVgrN33gBmgHAgOcLI7g2kSDt6mpg/view?usp=sharing)


#### 🛠 How to Run Locally & Develop ?
1. Install [Python](https://www.python.org/downloads/) and [Pipenv](https://pypi.org/project/pipenv/).
   If you had installed python and Pipenv previously, No need to re-install again.
2. Clone this repository and rename the folder as per your requirement.

  Your directory structure should appear as follows;
  ```structure
  StreamZ
      ├── system
      └── media
  ```
3. Installing **Requirements** is important. **(in root)**
   for Mac Users,
  ```requirements1
    python -m pip install -r requirements.txt 
  ```
  for Linux Users,
  ```requirements1
    pip install -r requirements.txt 
  ```
4. Navigate to **system/settings.py**, Change the Secret-key to your own project key and set Debug = True;
5. To run the server, Inside root use the command;
  ```
    python manage.py runserver
  ```
  For help with commands, Use the following;
  ```
    python manage.py help
  ```
6. Access the client at localhost **(http://127.0.0.1:8000)**

Check the #app/urls.py for accessable urls.
