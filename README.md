# Project Setup

## Details
1. JWT Auth
2. API Testing
3. Custom commands

## Prerequisites

Before begining, make sure the following prerequisites are installed on your system:

    Python (3.6 or higher)
    Docker (only if using Docker)
    Git
    pip

## Setup Process

### Option 1 - Using Docker

1. git clone git@github.com:Morvin-Ian/MiniBloggingApp-test.git

2. python manage.py migrate

3. docker-compose build

4. docker-compose up

### Option 2 - Without Docker

1. git clone git@github.com:Morvin-Ian/MiniBloggingApp-test.git

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
    

2. Login (two arguments - username, email, password) 

    ```
        python manage.py register 'email' 'password'

    ```

3. Logout (single argument - token)

    ```
        python manage.py logout 'token'

    ```

### Managing the Blogs

1. Fetch All the Blogs 

    ```
        python manage.py fetchblogs
    ```

2. Fetch A single the Blog (single argument - blog_id)

    ```
        python manage.py fetchblog <blog_id>
    ```

3. Create a new Blog (three arguments - title, content, token)

    ```
        python manage.py create 'title' 'content' 'token'
    ```

4. Update a Blog (four arguments - blog_id, title, content, token)

    ```
        python manage.py update <blog_id> 'title' 'content' 'token'

    ```

5. Delete a Blog (two arguments - blog_id, token)

    ```
        python manage.py update <blog_id> 'token'
    ```

    
