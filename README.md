## Prerequisites
- AWS CLI installed and configured
- AWS SAM installed
- Docker installed

## Installation steps
1. AWS CLI Installation Guide: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2. AWS CLI Configuration:
    - Run `aws configure` command and set required values
3. AWS SAM Installation Guide: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
   
## Setup and Deployment
```shell
git clone <repository-url>
cd <repository-directory>
```

After you have to put your env variable to file `template.yaml` line 29

## Commands to follow
```shell
sam build # will build image for you 
sam local invoke # will execute the function
sam deploy --guided # will help you to deploy your function
```

