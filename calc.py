import json
import boto3

client = boto3.client('ec2')

def termiate_ec2_instance(instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id
        ] 
    )
    return response

def send_message(sns_arn='arn:aws:sns:us-east-2:044248518213:test_email', subject='test of sending alert to an email', message  ="alert for cobra 11"):
        client_sns = boto3.client("sns")
        response = client_sns.publish(TopicArn=sns_arn, Message=message,object=subject)
        return response
        