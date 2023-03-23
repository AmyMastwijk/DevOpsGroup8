# DevOpsGroup8

The backlog of the Scrum board made with Trello is in the following files:
- Sprint1.json
- Sprint2.json
- Sprint3.json
- Sprint4.json

For adjusting the Load Balancer, the following two Lambda Functions were used:
- LambdaFunction_updateLoadBalancerToEC2.py
- LambdaFunction_updateLoadBalancerToLambda.py
  
The code of the Lambda function that handles the requests is in:
- LambdaFunction_handler.py
  
The Auto Scaling Group needs a Launch Configuration which uses the code from:
- user_data_Launch_Configurations.txt
