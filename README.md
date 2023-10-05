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

I. Registration (three arguments - username, email, password) 
  
    ```
        python manage.py register 'username' 'email' 'password'


    ```


II. Login (two arguments - username, email, password) 
    ```
        python manage.py register 'email' 'password'


    ```


III. Logout (single argument - token)
    ```
        python manage.py login 'token'


    ```

### Managing the Blogs

I. Fetch All the Blogs 
    ```
        python manage.py fetchblogs


    ```


II. Fetch A single the Blog (single argument - blog_id)
    ```
        python manage.py fetchblog <blog_id>



    ```

III. Create a new Blog (three arguments - title, content, token)
    ```
        python manage.py create 'title' 'content' 'token'


    ```

IV. Update a Blog (four arguments - blog_id, title, content, token)
    ```
        python manage.py update <blog_id> 'title' 'content' 'token'


    ```

V. Delete a Blog (four arguments - blog_id, token)
    ```
        python manage.py update <blog_id> 'token'

        
    ```