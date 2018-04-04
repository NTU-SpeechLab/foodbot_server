# foodbot_server
This is the web-hook, the backend to fulfill requests of the dialogflow v2 agent. Users send requests to dialogflow agent via web/Facebook messenger or other messenger platforms, they will receive the responses hard-coded in the dialogflow agent. This service is to provide alternative way, more flexible to response to users.
Find out more about fulfillment service here: https://dialogflow.com/docs/fulfillment



    Ubuntu 14.x
    Python 2.7

More about the dialogflow framework here: https://dialogflow.com/

# What is this service doing?

 * 

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

1. Update the path to logs folder (in src/mlogging/logging.json): should replace the actual path in your server, for example: 

    sys_log_dir/verbose.log => /local/foodchatbot/webUI/logs/errors.log

2. Prepare the database

  * Update the user/password for mysql: Notes on this line in src/intents/foods_order.py, fnb_data.py, fnb_definition.py
    
    engine = create_engine('mysql+mysqlconnector://root:<yourpassword>@localhost/canteena_fnb', pool_recycle=3600)
    
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


