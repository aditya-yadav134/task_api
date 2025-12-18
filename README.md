## Environment setup:
- Install Python 3.10.2
- Use any Code editor

## Installation steps:
- Open Terminal<br>

- Make a directory at any location and go inside directory <br>
    ``` mkdir <dir_name> && cd <dir_name> ```<br>

- Clone this repository <br>
    ```git clone https://github.com/aditya-yadav134/task_api.git ```<br>

- Go into 'task_api' directory :<br>``` cd task_api ```

- Install 'pipenv' for creating virtual environments and downloading required packages<br>
    ``` pip install pipenv ```<br>

- Create a virtual environment<br>
  ```pipenv shell```<br>

- Install all packages from __requirements.txt__ using pip<br>
    ```pipenv run pip install -r requirements.txt```

- Run below command to check if any migrations to be applied <br>
    ```python manage.py makemigrations```

- If any migrations shows then run the below command to migrate the database <br>
    ```python manage.py migrate```
 - Create a Admin user as follow __:__ <br>
    ```python manage.py createsuperuser```
    > Proide user name, email and password for successful account creation.

- Run the server for testing the API <br>
    ```python manage.py runserver```


 ## Testing API in Postman  

- Now I will be using __Postman__ to test the API. Go to official page of Postman to download it on your computer. <br>

 - We will be using __"Admin"__ user to create 2-3 tasks so that we can test different endpoints <br>
 
 - __Login using username and password used previously for __Admin__ user__ <br>
   
   + In address bar select 'POST' and type url __:__  <br> http://127.0.0.1:8000/api/auth/login    

   + Click on 'Body' tab and enter following:<br>
        ```
        {
            "username" : "Admin user name",
            "password" : "Admin password"
        }
        ```
   + We will get __JWT tokens__ for login (access) and refresh
       
       ```
       {
         "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ", 
          "refresh": "eyJ0b2tlbl90eXBlIjoicmVmcmVza",
          "user": {
            "pk": 2,
            "username": "test",
            "email": "",
            "first_name": "",
            "last_name": ""
            }
      }
      ```
  
- __Use JWT tokens in requests (with headers)__
    
    - In address bar select 'GET' and type url:<br>
     " http://127.0.0.1:8000/api/tasks/"
    
    - Click on 'Authorization' tab and enter following:<br>
           ```Type : Bearer Token
           ```<br>
           ```Token : Paste access token value from the previous step for this user
           ```
    
    - We will get all tasks made by this user __:__<br>
        ```
             {
                "id": 7,
                "title": "Task 5",
                "description": "Task 5 modified by admin",
                "status": true,
                "owner": 3
              }
        ```  
- __Register a user :__<br>
      
    + In address bar select 'POST' and type url __:__ <br> 
     __http://127.0.0.1:8000/api/auth/register/__

    + Click on __Body__ tab and enter following: <br>
        ``` 
             {
              "username" : "test2",
              "password1" : "Vartak2025"
              "password2" : "Vartak2025"
             }

        ```
    + Click __Send__ and we will get respose similar to this __:__ <br>
        ```     
            {
                "access" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" ,
                 "refresh": "e0.Me6-V8Nv8PWco5AQDs8JU7f4DtbYfcelgGtcIRgjK8U" ,
                 "user": {
                            "pk": 5,
                            "username": "test3",
                            "email": "",
                            "first_name": "",
                            "last_name": ""
                         }
             } 
        ```
  
  ##    List of all main API endpoints
  
  ### 1.  Authentication: <br>
    
    + **POST** ```/api/auth/register/``` **:** <br>
             Takes username, password1, password2 and give response containing values for __access__ and __refresh__ token <br>
             
    +   **POST** ```/api/auth/login/``` **:** <br>
              Takes username, password and match values on server if correct give response containing values for __access__ and __refresh__  token <br>  
    
    +   **POST** ```/api/auth/logout/``` **:** <br>
              Logout user from API by destroying access token on the server <br>
    
    +   **POST** ```/api/auth/refresh/``` **:** <br>
              Takes 'refresh' token value and server validates it and response with new value for 'access' token <br>

  ### 2.   __Tasks__ : <br>
    
    *   **GET** ```/api/tasks/``` : <br>
        List all the __Tasks__ created if user is __Admin__ otherwise list all tasks of that user.

    *   **POST** ```/api/tasks/``` : <br>
      Creates a new tasks and also set owner of task to current user

    *   **GET** ```/api/tasks/<id>/``` : <br>
      Return response containing values for attributes of "Task".

    *   **PUT/PATCH** ```/api/tasks/<id>/``` : <br>
      
        + **PUT** :- Updates values of __Tasks__ object from data contained in the request. <br>If values for some attributes are provided then those attributes will get updated other values remain the same. <br>
      
        +  **PATCH** :- Updates __Tasks__ object completely. If some attribute values are not present in the request then __Tasks__ will have empty values for those attributes.

    *   **DELETE** ```/api/tasks/<id>/``` :- <br>
        Delete the __Task__ from the database. 
        This only happens if requesting User is __Admin__ or tasks is created by him.
       
