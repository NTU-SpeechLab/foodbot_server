# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

from mlogging.mlogger import logger
from methods_mapping import methods
import resources.sample_data_strings as ConstStr
import pprint


app = Flask(__name__, static_url_path="")
api = Api(app)
auth= HTTPBasicAuth()

__DEBUG__ = True

@auth.get_password
def get_password(username):
    if username == 'chatbot':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    logger().error(ConstStr.unauthorized_access)
    return make_response(jsonify({"error": ConstStr.unauthorized_access}), 403)


#------------------------------------------------#
request_fields = {
    'responseId': fields.String,
    'queryResult': fields.Nested,
    'webhookStatus': fields.Nested,
    'uri': fields.Url('request')
}


def format_dialogflow_text(inputStrArr):
    textOutputs = []
    for response in inputStrArr:    
        textOutputs.append({
          "text": {
            "text": [response]
          }
        })
    return textOutputs

def format_dialogflow_qR(quickReplies):
    if (quickReplies == None):
        return

    quickRepliesOutputs = {
      "quickReplies": {
        "title": quickReplies[0],
        "quickReplies": quickReplies[1:],
      }
    }
    return [quickRepliesOutputs]

def format_dialogflow_cards(cards):
    if (cards == None):
        return

    if (len(cards)%2 != 0):
        return

    cardOutputs = []
    for i in xrange(len(cards)/2):
        cardOutputs.append({
          "card": {
            "title": cards[i*2],
            "imageUri": cards[i*2 + 1],
          },
          #"platform": "FACEBOOK"
        })
    return cardOutputs

def get_user_id(response_json):
    if (__DEBUG__):
        print ("GET_USER_ID")
        pprint.pprint(response_json)
        print ("GET_USER_ID")

    user_id = ""
    if (type(response_json) == type([])):
        for context in response_json:
            if not ('parameters' in context.keys()):
                continue

            ctx_parameters = context['parameters']
            if "facebook_sender_id" in ctx_parameters:
                user_id =  ctx_parameters['facebook_sender_id']
                return user_id
    else:
        ctx_parameters = response_json['parameters']
        if "facebook_sender_id" in ctx_parameters:
            user_id =  ctx_parameters['facebook_sender_id']
            return user_id
    return user_id


class ApiaiRequestAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('responseId', type = str, required = True, help = 'No post request id?', location = 'json')
        self.reqparse.add_argument('queryResult', type = dict, default = "", help='No results from dialogflow?', location = 'json')
        self.reqparse.add_argument('webhookStatus', type = dict, default = "", help='No status from dialogflow?', location = 'json')

    def get(self):
        #return {'request': [marshal(request, request_fields) for request in requests]}
        pass

    def post(self):
        args = self.reqparse.parse_args()
        # 1. Check if the session id is new or old - meaning the different person or timeout
        if (__DEBUG__):
            print ("Receiving request from facebook-dialogflow")
            pprint.pprint(args)
            print ("Finished receiving from facebook-dialogflow")

        ########################################
        # Process the information from api.ai
        ########################################
        # 1. Check if the session id is new or old - meaning the different person or timeout
        sessionId = args["responseId"]
        logger("webhookInterface").info("Current session id is " + sessionId)
        if (__DEBUG__):
            print("Current session id is " + sessionId)

        result = dict(args["queryResult"])

        # 2. Output context, should save in backend for future processing
        intent_name_confident_score = (result["intentDetectionConfidence"])
        function_name_from_intent = ""
        context_user_id = sessionId
        parameters = {}

        if ("intent" in result.keys()):
            function_name_from_intent = str(result["intent"]["displayName"])
            parameters = dict(result["parameters"])

            if ('outputContexts' in result.keys()):
                context_user_id = get_user_id(result["outputContexts"])
                if (__DEBUG__):
                    pprint.pprint(result['outputContexts'])
                    print ("Finished processing user id ")
                    pprint.pprint(context_user_id)

            logger("webhookInterface").debug(type(parameters))
            if (len(parameters.values()) > 0):
                logger("webhookInterface").debug(parameters.values()[0])
            logger("webhookInterface").info("--------------------------")
            logger("webhookInterface").info(parameters.values())
            logger("webhookInterface").info("--------------------------")


            # 3. Original query, provide more information, maybe contain the info that api.ai doesn't recognize
            reslt_query = str(result["queryText"])
            logger("webhookInterface").info("Resolved query is " + reslt_query)

            # 4. Action associated with the query (checking map, database, etc.)
            #reslt_action = str(result["action"])

            # 5. Get the intent name, call the function named as intent to get the result
            logger("webhookInterface").info("Call the function " + function_name_from_intent  + "(" + str(parameters.values()) + ")")
            if (__DEBUG__):
                print("Call the function " + function_name_from_intent  + "(" + str(parameters.values()) + ")")
            webhookResponses = {"text": ConstStr.unknown_input_str1}

            if function_name_from_intent in methods:
                func_params = parameters.values()
                func_params.append(context_user_id)
                if (__DEBUG__):
                    print ("Parameters pass to the function: ")
                    pprint.pprint(func_params)
                webhookResponses = methods[function_name_from_intent](func_params) # + argument list of course
            else:
                if ("smalltalk" in function_name_from_intent):
                    logger("webhookInterface").info("No need webhook")
                else:
                    raise Exception("Method %s not implemented" % function_name_from_intent)

            # 6. Return the result: Form the result conform with the request.
            if webhookResponses == None:
                logger("webhookInterface").info("There is no response from webhook")
                return {
                    "fulfillmentText": webhookResponses,
                    "fulfillmentMessages": [{
                        "text": {
                          "text": [webhookResponses]
                        }
                    }],
                    "source": "webhookInterface",
                    "payload": {},
                    "outputContexts": [],
                    "followupEventInput": {}
                    }
            else:
                logger("webhookInterface").info("Response from webhook is: ")
                if (__DEBUG__):
                    pprint.pprint(webhookResponses)
                    print("Return format")

                fullReps = format_dialogflow_text(webhookResponses['text'])
                if ('quickReplies' in webhookResponses.keys()):
                    fullReps = fullReps + format_dialogflow_qR(webhookResponses['quickReplies'])
                if ('cards' in webhookResponses.keys()):
                    fullReps = fullReps + format_dialogflow_cards(webhookResponses['cards'])

                if (__DEBUG__):
                    pprint.pprint(fullReps)

                if (type(webhookResponses) == type({})):
                    return {
                        "fulfillmentText": webhookResponses['text'][0],
                        "fulfillmentMessages": fullReps,
                    "source": "webhookInterface",
                    "payload": {},
                    "outputContexts": [],
                    "followupEventInput": {}
                    }
                else:
                    return {
                        "fulfillmentText": webhookResponses,
                        "fulfillmentMessages": [{
                            "text": {
                              "text": [webhookResponses]
                            }
                            }],
                        "source": "webhookInterface",
                        "payload": {},
                        "outputContexts": [],
                        "followupEventInput": {}
                        }


api.add_resource(ApiaiRequestAPI, '/foodorder/api/v1.0/requests', endpoint = 'requests')


import os
if __name__ == "__main__":
    cwd = os.getcwd()
    os.environ["PYTHONPATH"] = cwd
    app.run(debug=True, host='0.0.0.0', port=3010)
