## Instructions to Run App

* Follow the instructions on the README.md file of the [flask pymongo repository](https://github.com/nyu-software-engineering/flask-pymongo-web-app-example) to create the local database, make a .env file, make a virtual environment, install dependencies, run flask, etc.
* The general procedure should be as follows:
    * Open command prompt and run the following command to create the database, if you are using docker: 
        ```
        docker run --name mongodb_dockerhub -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secret -d mongo:latest
        ```
    * Run the following command to make sure that you can access the database:
        ```
        docker exec -ti mongodb_dockerhub mongosh -u admin -p secret
        ```
    * Create a .env file with the following fields (the db name and uri may change based on how you created the local db):
        ```
        FLASK_APP=app.py
        FLASK_ENV=development
        MONGO_DBNAME=example
        MONGO_URI="mongodb://admin:secret@localhost:27017/example?authSource=admin&retryWrites=true&w=majority"
        ```