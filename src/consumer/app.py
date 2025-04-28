import json
import boto3
import os
import base64

# DynamoDB client
dynamodb = boto3.resource('dynamodb')

# DynamoDB table name
DYNAMODB_TABLE_NAME = os.environ['DYNAMODB_TABLE_NAME']

# Reference to the DynamoDB table
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the record from base64 and parse JSON
        #payload = json.loads(record['kinesis']['data'])

        # Base64 decode first, then JSON parse
        decoded_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        payload = json.loads(decoded_data)
        
        # Insert the event data into DynamoDB
        try:
            response = table.put_item(
                Item=payload  # Assuming payload contains the entire event data
            )
            print(f"Successfully inserted event into DynamoDB: {response}")
        
        except Exception as e:
            print(f"Error inserting event into DynamoDB: {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Event successfully processed!'})
    }
