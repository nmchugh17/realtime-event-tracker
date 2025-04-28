import json
import boto3
import os

# DynamoDB client
dynamodb = boto3.resource('dynamodb')

# DynamoDB table name
DYNAMODB_TABLE_NAME = os.environ['DYNAMODB_TABLE_NAME']

# Reference to the DynamoDB table
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

def lambda_handler(event, context):
    # Scan DynamoDB table to fetch all records
    try:
        response = table.scan()
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'body': json.dumps({'items': items})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error occurred', 'error': str(e)})
        }
