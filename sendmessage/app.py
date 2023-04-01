import json
import boto3
import openai
import os


def lambda_handler(event, context):
    # Get OpenAI API key from env
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Get input message and connectionId
    data = json.loads(event.get('body', '{}')).get('data')
    domain_name = event.get('requestContext', {}).get('domainName')
    stage = event.get('requestContext', {}).get('stage')
    connectionId = event.get('requestContext', {}).get('connectionId')
    apigw_management = boto3.client(
        'apigatewaymanagementapi', endpoint_url=F"https://{domain_name}/{stage}")

    # Request ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": data},
        ],
        stream=True
    )

    # Send message to client
    for partial_message in response:
        content = partial_message['choices'][0]['delta'].get('content')
        if content:
            apigw_management.post_to_connection(
                ConnectionId=connectionId, Data=content)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "data sent.",
        }),
    }
