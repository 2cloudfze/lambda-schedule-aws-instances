# EC2 Start/Stop Lambda Functions
This project contains AWS Lambda functions to start and stop EC2 instances using AWS Lambda and Auto Scaling capabilities.

## Table of Contents
* Prerequisites
* Installation
* Configuration
* Usage
* Contributing

## Prerequisites
* AWS account with appropriate permissions to create and manage Lambda functions, EC2 instances, and Auto Scaling groups.
* Python 3.7 or above.

## usage

* The Start Instances Lambda function starts the stopped EC2 instances and updates the desired capacity of the Auto Scaling group.
* The Stop Instances Lambda function stops the running EC2 instances and updates the desired capacity of the Auto Scaling group.

## Configuration

1. Log in to your AWS Management Console.

2. Navigate to the AWS Lambda service.

3. Click on the "Create function" button.

4. Choose "Author from scratch."

5. Enter a name for your "Start EC2 Instances" function, choose "Python 3.7" as the runtime, and select "Create a new role" for the execution role with below policy.

```{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "ec2:DescribeInstances",
                "ec2:DescribeTags",
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "ec2:DescribeInstanceStatus",
                "autoscaling:UpdateAutoScalingGroup"
            ],
            "Resource": "*"
        }
    ]
}```

6. Click "Create function" to create the function.

7. In the function details page, scroll down to the "Function code" section, and copy-paste the code from the file `ec2start.py` in this repository.

8. Click "Save" to save the function code.

9. Repeat steps 3 to 8 to create the "Stop EC2 Instances" function, using the code from the file `ec2stop.py`.

10. Navigate to the Amazon CloudWatch service.

11. Click on "Rules" in the left-hand menu and then click "Create rule."

12. Set up a rule to trigger the "Start EC2 Instances" function at the desired schedule, e.g., every weekday at 8 AM. You can use a cron expression like `0 8 ? * MON-FRI`.

13. Set up another rule to trigger the "Stop EC2 Instances" function at the desired schedule, e.g., every weekday at 6 PM. You can use a cron expression like `0 18 ? * MON-FRI`.

14. Save each rule.

15. Verify that the Lambda functions are working correctly by checking the CloudWatch Logs for any errors or successful executions.

## Function Descriptions
Before running the Lambda functions, you need to configure the following:

* Replace the webhook_url variable in the lambda_handler function with the URL of your Slack webhook for notifications.
* Set the appropriate region for the EC2 instances and Auto Scaling group by updating the region_name parameter in the code.
* Update the auto_scaling_group_name variable with the name of your Auto Scaling group.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
