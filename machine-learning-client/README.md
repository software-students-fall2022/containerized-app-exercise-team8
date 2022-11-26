## Instructions to set up database

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
        MONGO_DBNAME=example
        MONGO_URI="mongodb://admin:secret@localhost:27017/example?authSource=admin&retryWrites=true&w=majority"
        ```