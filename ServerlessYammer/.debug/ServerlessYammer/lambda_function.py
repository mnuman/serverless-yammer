import json
import os
import requests
def lambda_handler(event, context):
    print(json.dumps(event))
    
    body = json.loads(event['body'])
    myMessage = f"Hi, {body['head_commit']['author']['name']} has just committed code at {body['head_commit']['url']} with message {body['head_commit']['message']}"
    auth = { "Authorization" : "Bearer " + os.environ['YAMMER_KEY']}
    payload = { "body" : myMessage, "group_id" : 15767042} 
    r = requests.post("https://www.yammer.com/api/v1/messages.json", headers=auth, data=payload)

    print("Status code Yammer call:" + str(r.status_code))
    
    return {
        "isBase64Encoded" : "false",
        "statusCode" : 200,
        "headers" : {},
        "body" : json.dumps(myMessage)
    }