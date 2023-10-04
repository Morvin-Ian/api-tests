# MiniBloggingApp-test

## Prerequisites

Before begining, make sure the following prerequisites are installed on your system:

    Python (3.6 or higher)
    Docker (only if using Docker)
    Git
    pip
## Setup Process
### Option 1 - Using Docker
1. git clone https://github.com/Morvin-Ian/MiniBloggingApp-test.git

2. python manage.py migrate

3. docker-compose build

4. docker-compose up

### Option 2 - Without Docker

1. git clone https://github.com/Morvin-Ian/MiniBloggingApp-test.git

2. pip install -r requirements.txt 

3. python manage.py migrate

4. Navigate to the settings.py file in the project folder and set USING_DOCKER attribute to False
    ```
        # settings.py
        USING_DOCKER = False
    ```
5. python manage.py createcachetable

6. python manage.py runserver


## Running Tests
1. Navigate to the settings.py file in the project folder and set USING_DOCKER attribute to False
    ```
        # settings.py
        USING_DOCKER = False
    ```
2. python manage.py test