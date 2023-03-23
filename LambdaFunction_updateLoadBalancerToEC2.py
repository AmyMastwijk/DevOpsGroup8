import json
import boto3

def lambda_handler(event, context):
    # Set up the AWS SDK client for Elastic Load Balancing (ELBv2)
    elbv2 = boto3.client('elbv2')

    # Set the ALB arn and listener arn
    alb_arn = 'arn:aws:elasticloadbalancing:eu-central-1:401827531924:loadbalancer/app/TestWebServerScaling/a72e73d3bf1f29c6'
    listener_arn = 'arn:aws:elasticloadbalancing:eu-central-1:401827531924:listener/app/TestWebServerScaling/a72e73d3bf1f29c6/67b0ab988e54b831'

    # Update the listener rules for the specified listener
    updatedRule = elbv2.modify_rule(
        RuleArn='arn:aws:elasticloadbalancing:eu-central-1:401827531924:listener-rule/app/TestWebServerScaling/a72e73d3bf1f29c6/67b0ab988e54b831/e61ef29d58b5a1b5',
        Actions=[
                {
                    'Type': 'forward',
                    'TargetGroupArn': 'arn:aws:elasticloadbalancing:eu-central-1:401827531924:targetgroup/TestInstancesScaling/1b207056e326ea05'
                }
            ]
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Listener action updated to redirect to EC2')
    }
