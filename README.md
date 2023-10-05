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

4. Navigate to the settings.py file in the project folder and set USE_REDIS attribute to False
    ```
        # settings.py
        USE_REDIS = False
    ```
5. python manage.py createcachetable

6. python manage.py runserver


## Running Tests
1. Navigate to the settings.py file in the project folder and set USE_REDIS attribute to False
    ```
        # settings.py
        USE_REDIS = False
    ```
2. python manage.py test

## Consuming the Api through the console command
### Authentication
```
  Always note the token and copy it as you will use it to create, delete, or update blogs.
```

1. Registration (three arguments - username, email, password) 
  
    ```
        python manage.py register 'username' 'email' 'password'

    ```  
    
![register](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/81d720ed-d029-428a-ae6b-fe94e812334d)

2. Login (two arguments - username, email, password) 

    ```
        python manage.py register 'email' 'password'

    ```
![login](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/618cd6a5-9ae0-4e76-a552-0b5889afb2b4)

3. Logout (single argument - token)

    ```
        python manage.py login 'token'

    ```

### Managing the Blogs

1. Fetch All the Blogs 

    ```
        python manage.py fetchblogs
    ```
![fetchall](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/ac4808a6-b2fe-4505-a164-dd4d76e11083)

2. Fetch A single the Blog (single argument - blog_id)

    ```
        python manage.py fetchblog <blog_id>
    ```
![fetchsingle](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/6c3260d4-80a1-419e-9672-b1dad4beedc6)

3. Create a new Blog (three arguments - title, content, token)

    ```
        python manage.py create 'title' 'content' 'token'
    ```
![create](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/56a6e544-86ab-4bcb-b5d9-03cd1c291561)

4. Update a Blog (four arguments - blog_id, title, content, token)

    ```
        python manage.py update <blog_id> 'title' 'content' 'token'

    ```
![update](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/f88925a6-c840-4cad-9457-bf966043958d)

5. Delete a Blog (four arguments - blog_id, token)

    ```
        python manage.py update <blog_id> 'token'
    ```
![delete](https://github.com/Morvin-Ian/MiniBloggingApp-test/assets/78966128/d0f613b8-c0e6-40f2-8b24-d4adeb657f36)

    
