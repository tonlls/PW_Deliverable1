# PW_Deliverable1
This project is deployed on https://deliverable1.herokuapp.com/

With superuser:

`username -> admin`

`password -> admin`

To build for docker you can run:

`docker-compose up --build -d`

To run the server locally you can run 

`python manage.py runserver`

## The github repository is:

https://github.com/tonlls/PW_Deliverable1

## Nlayer proposal:

1. It has 3 servers.
    - Web: This server will contain the frontend and will connect to the backend throught the API.
    - Backend: This server will contain the backend, the logic of our application implemented as an API and will be connected to de database throught a database connector.
    - Database: This server will contain the database, wich can be relational or not relational since the connector will be on charge of interacting directly within the database.
2. The Backend depends on the database, and the web depends on the backend to get the data.
3. The only optional one is the Web.

## Users
https://github.com/tonlls
https://github.com/IanRibaltaGene
https://github.com/incipasa