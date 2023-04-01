# ServerlessChatGPTStream

Make ChatGPT API stream call in a serverless environment using AWS API Gateway(WebSocket API) and Lambda.

## Requirements
- AWS Account
- [AWS Serverless Application Model (AWS SAM) CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- [OpenaiApiKey](https://platform.openai.com/account/api-keys)
- (optional) [wscat](https://github.com/websockets/wscat)

## Build & Deploy
```bash
sam build --use-container
sam deploy --guided
```

### Sample arguments for 'sam deploy'
```
Stack Name [sam-app]: serverlesschatgpt
AWS Region [ap-northeast-1]: ap-northeast-1
Parameter OpenaiApiKey []: sk-xxxx
#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
Confirm changes before deploy [y/N]: N
#SAM needs permission to be able to create roles to connect to the resources in your template
Allow SAM CLI IAM role creation [Y/n]: Y
#Preserves the state of previously provisioned resources when an operation fails
Disable rollback [y/N]: N
Save arguments to configuration file [Y/n]: Y
SAM configuration file [samconfig.toml]: samconfig.toml
SAM configuration environment [default]: default
```

## Test
When the deployment is complete, you will see the following message.
```
Key                 ChatGPTWebSocketEndpoint
Description         API Gateway endpoint URL for Prod stage for ServerlessChatGPTStream                              
Value               wss://hhyd8fkhtl.execute-api.ap-northeast-1.amazonaws.com/Prod
```

Now you can test the endpoint using wscat.

```bash
$ wscat -c wss://hhyd8fkhtl.execute-api.ap-northeast-1.amazonaws.com/Prod
Connected (press CTRL+C to quit)
> {"action":"sendmessage", "data":"hi"}
< Hello
< !
<  How
<  can
<  I
<  assist
<  you
<  today
< ?
>
```


## Delete
```bash
sam delete --stack-name serverlesschatgpt
```
