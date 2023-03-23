import json

def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST",
        "X-Generated-By": "Lambda_Function",
        "Access-Control-Expose-Headers": "X-Generated-By",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    if http_method is None:
        return {
            "statusCode": 400,
            "statusDescription": "400 Bad Request",
            "isBase64Encoded": False,
            "headers": headers,
            "body": json.dumps({"message": "httpMethod is not defined in the request."})
        }

    if http_method == 'OPTIONS':
        return {
            "statusCode": 200,
            "statusDescription": "200 OK",
            "isBase64Encoded": False,
            "headers": headers,
            "body": ""
        }

    if http_method != 'POST':
        return {
            "statusCode": 405,
            "statusDescription": "405 Method Not Allowed",
            "isBase64Encoded": False,
            "headers": headers,
            "body": json.dumps({"message": "Only POST requests are allowed."})
        }

    return {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": headers,
        "body": json.dumps({"message": "Success"})
    }
