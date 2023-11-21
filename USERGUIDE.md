# Backend

This project was built using python. ORM used was sqlalchemy

## Accomplishments
- The majority of the features were achieved
- An ORM was used to process the data from the database. Only queries to BigQuery had to be raw SQL due to the used library 
- Classes, functions, services were documented for enabling other developers to contribute more easily
- Relations are used to enhance SQL queries and performance
- Environment variables were used to keep the application safe when deploying

https://www.youtube.com/watch?v=hK5ZHxyg1cA

# Userguide

Unfortunately, I couldn't run the front inside the Docker container.
Therefore, to check the functionality of the application you must:

Use node 18+
Run activate.sh for the environment variables and run the docker-compose that contains the DB and the back
Run npm run dev in the front folder
