# foodbot_server
This is the web-hook, the backend to fulfill requests of the dialogflow v2 agent. Users send requests to dialogflow agent via web/Facebook messenger or other messenger platforms, they will receive the responses hard-coded in the dialogflow agent. This service is to provide alternative way, more flexible to response to users.
Find out more about fulfillment service here: https://dialogflow.com/docs/fulfillment



    Ubuntu 14.x
    Python 2.7

More about the dialogflow framework here: https://dialogflow.com/

# What is this service doing?

 * Receiving JSON request from dialogflow, and format this request, extract the intent/entities from this JSON request
 * Mapping the intent name with defined function in the list -> call this function to get response 
 * Can return the response in text, basic cards (images), and quick replies.
 

# Dependencies
List of packages required to install before running the client:

    pytz   
    python-dateutil   
    sqlalchemy   
    flask   
    flask_restful
    flask_httpauth
    mysql-python
    mysql-connector (pip install mysql-connector-python)
    apiai   
    pyenchant   
    wtforms   
    ntlk

# Notes before running

1. Update the path to logs folder (in src/mlogging/logging.json, renaming logging_template.json to logging.json): should replace the actual path in your server, for example you put your code to /local/foodchatbot/webUI, then the path must be updated to: 

    
         sys_log_dir/verbose.log => /local/foodchatbot/webUI/logs/verbose.log
         sys_log_dir/info.log => /local/foodchatbot/webUI/logs/info.log
         sys_log_dir/errors.log => /local/foodchatbot/webUI/logs/errors.log

2. Prepare the database

  * Update the user/password for mysql: Notes on this line in src/intents/foods_order.py, fnb_data.py, fnb_definition.py
    
        $ engine = create_engine('mysql+mysqlconnector://<your_sql_username>:<your_sql_password>@localhost/canteena_fnb', pool_recycle=3600)
    
    
  * Create the database named 'canteena_fnb'
  
  * Running these scripts to populate data to tables
  
  
        $ python fnb_definition.py
        $ python fnb_data.py


# Running the web service - server
Go to src folder and running the command

    $ python webhookInterface.py

Check the result at http://localhost:3010/foodorder/api/v1.0/requests
The page is loaded with JSON format, and null in the content.

This address should be publish to public address, and put to the agent's fulfillment setting. You can use the ngrok to navigate this address to public one:

    $ ./ngrok http 3010 -bind-tls=true
    
Then you can copy the public address with https to your agent.


