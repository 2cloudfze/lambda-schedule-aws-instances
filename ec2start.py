import boto3
import logging
import json
import requests
webhook_url = "your webhookurl"

#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#define the connection
ec2 = boto3.resource('ec2', region_name='eu-north-1')
auto_scaling_client = boto3.client('autoscaling')

def update_auto_scaling_group(auto_scaling_group_name):
    response = auto_scaling_client.update_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group_name,
        MinSize=1,
        MaxSize=1,
        DesiredCapacity=1
    )
    print(f'Updated Auto Scaling group: {auto_scaling_group_name} to its capacity')
    return response


def lambda_handler(event, context):

    # all stopped EC2 instances.
    filters = [{
            'Name': 'tag:AutoStart',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['stopped']
        }
    ]
    
    #filter the instances
    instances = ec2.instances.filter(Filters=filters)

    #locate all stopped instances
    RunningInstances = [instance.id for instance in instances]
    

    #print StoppedInstances 
    
    if len(RunningInstances) > 0:
        #perform the startup
        AutoStarting = ec2.instances.filter(InstanceIds=RunningInstances).start()
        print(AutoStarting)
        # Update the Auto Scaling group to zero capacity
        auto_scaling_group_name = 'your_auto_scaling_group_name'
        update_auto_scaling_group(auto_scaling_group_name)

        # Send Slack notification
        
        slack_message = {"text": "*Client* : Omnyex\n*Notification* : Starting EC2instances\n*Instances* : m2omnit,m2varnish"}
        response = requests.post(webhook_url, data=json.dumps(slack_message))
        return response.text
    else:
        print("Nothing to see here")
        slack_message = {'text': 'EC2 not started\ninstances have already started.'}
        response = requests.post(webhook_url, data=json.dumps(slack_message))
        return response.text
