# PW_Deliverable1
this project is deployed on https://deliverable1.herokuapp.com/
with superuser:

`username -> admin`

`password -> admin`

to build for docker you can run:

`docker-compose up --build -d`

to run the server locally you can run 

`python manage.py runserver`

## The github repository is:

https://github.com/tonlls/PW_Deliverable1

## Nlayer proposal:

1. It has 3 servers.
    - Web: this server will contain the frontend and will connect to the backend throught the API
    - Backend: this server will contain the backend, the logic of our application implemented as an API and will be connected to de database throught a database connector
    - Database: this server will contain the database wich can be relational or not relational since the connector will be on charge of interacting directy within the database 
2. backend is dependend on the database and the web is dependent on the backend to get data.
3. the only optional one is the Web.
