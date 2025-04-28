import json
import boto3
import os

# Kinesis client
kinesis_client = boto3.client('kinesis')

# The name of the Kinesis stream
KINESIS_STREAM_NAME = os.environ.get('KINESIS_STREAM_NAME')

def lambda_handler(event, context):

    try:
        # Parse the event data from the API gateway request body
        event_data = json.loads(event['body'])

        # Put the event data into the kinesis data stream
        response = kinesis_client.put_record(
            StreamName=KINESIS_STREAM_NAME,
            Data=json.dumps(event_data),  # Data to send to Kinesis
            PartitionKey="partitionkey"
            )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Event successfully sent to Kinesis!', 'response': response})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error occurred', 'error': str(e)})
        }

