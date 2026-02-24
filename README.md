Welcome to Support4U:

Running the application
***********************

First you will need to create a virtual environment.

To download my dependencies stored in the 'requirements.txt' file, put the following command into your terminal:

1. pip install -r requirements.txt

To run my application, you will need to create a .env file. This should contain your SECRET_KEY. In addition it should include both databases: TESTING and DATABASE. Please see .env.example.

Then to run the application and the put the following command into your terminal:

1. 'python app.py'

The application should now be locally running on localhost:5000

Deployed application on Render
******************************

Link to deployed application: https://support4u.onrender.com

This auto-deploys when a change has been made on the 'main' branch in my gitHub repo.

Lecturer testing purpose:
*************************

An example of an admin account to login as (case-sentitive):

Username: Nathan
password: nathan

Testing:
********

To run my pytests tests put the following command into the terminal:

1. pytests

To run my cypress tests put the following command into the terminal:

1. npx cypress open

