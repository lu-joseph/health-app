# health-app

## Setup:

If you don't have PostgreSql, install it [here](https://www.postgresql.org/download/)

- Install with all defaults and remember the password you set
- 
Create a database:

- Open SQL Shell (psql)
- Login by using the defaults (click enter each time) and enter the password chosen during installation
- Once logged in, type `CREATE DATABASE <name>`, where `<name>` is the name of your local database

Set up the environment
- Create a copy of `.env.sample` and rename it to `.env`
- Fill in `.env` with the correct data for your local psql setup
- In the console, navigate to the backend folder and type the following commands:
```
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Running the app in Windows:
  - In the console, ensure you are in the backend folder
  - Ensure the virtual environment is activated (with `venv\Scripts\activate`)
  - Enter the command `flask run`


