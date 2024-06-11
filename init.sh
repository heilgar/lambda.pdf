#!/bin/bash

# Variables
STACK_NAME="lambda-pdf"
TEMPLATE_FILE="template.yaml"
GIT_DIR="."
CODECOMMIT_REPO_NAME="lambda-pdf"
BUILD_PROJECT_NAME="lambda-pdf"
REGION="us-east-1"

# Deploy CloudFormation stack
echo "Deploying CloudFormation stack..."
aws cloudformation create-stack --stack-name $STACK_NAME --template-body file://$TEMPLATE_FILE --capabilities CAPABILITY_IAM
aws cloudformation wait stack-create-complete --stack-name $STACK_NAME
echo "Stack deployed."

# Get the CloneUrlHttp for the CodeCommit repository
CLONE_URL=$(aws codecommit get-repository --repository-name $CODECOMMIT_REPO_NAME --query 'repositoryMetadata.cloneUrlHttp' --output text)

# Remove existing git directory
if [ -d "$GIT_DIR/.git" ]; then
  echo "Removing existing .git directory..."
  rm -rf "$GIT_DIR/.git"
  echo "Removed existing .git directory."
fi

# Initialize a new git repository
echo "Initializing new git repository..."
cd $GIT_DIR
git init
git remote add origin $CLONE_URL

# Commit files to the new CodeCommit repository
echo "Committing files to CodeCommit repository..."
git add .
git commit -m "Initial commit"
git push -u origin master
echo "Files committed."
