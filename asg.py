import boto3
import logging
import json
import requests

webhook_url = "https://hooks.slack.com/services/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"
# Setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define the connection and set the region
ec2 = boto3.resource('ec2', region_name='eu-west-1')
auto_scaling_client = boto3.client('autoscaling')

def update_auto_scaling_group(auto_scaling_group_name):
    response = auto_scaling_client.update_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group_name,
        MinSize=0,
        MaxSize=0,
        DesiredCapacity=0
    )
    print(f'Updated Auto Scaling group: {auto_scaling_group_name} to zero capacity')
    return response

def lambda_handler(event, context):
    # All running EC2 instances.
    filters = [{
            'Name': 'tag:AutoStop',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    
    # Filter the instances which are stopped
    instances = ec2.instances.filter(Filters=filters)

    # Locate all running instances
    running_instances = [instance.id for instance in instances]
    
    if len(running_instances) > 0:
        # Perform the shutdown
        shutting_down = ec2.instances.filter(InstanceIds=running_instances).stop()
        print(shutting_down)
        
        # Update the Auto Scaling group to zero capacity
        auto_scaling_group_name = 'tet2'
        update_auto_scaling_group(auto_scaling_group_name)
        
        # Send Slack notification
        slack_message = {
            "text": "*Client* : Omnyex\n*Notification* : Stopping EC2 instances\n*Instances* : m2omnit, m2varnish"
        }
        response = requests.post(webhook_url, data=json.dumps(slack_message))
        return response.text
    else:
        print("Nothing to see here")
        slack_message = {'text': 'EC2 instances have already stopped.'}
        response = requests.post(webhook_url, data=json.dumps(slack_message))
        return response.text
