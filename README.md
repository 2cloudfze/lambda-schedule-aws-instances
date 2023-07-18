# EC2 Start/Stop Lambda Functions
This project contains AWS Lambda functions to start and stop EC2 instances using AWS Lambda and Auto Scaling capabilities.

## Prerequisites
1. AWS account with appropriate permissions to create and manage Lambda functions, EC2 instances, and Auto Scaling groups.
2. AWS CLI installed and configured with your AWS account credentials.
3. Python 3.7 or above.

## Configuration
Before deploying the Lambda functions, make sure to configure the following:

1. Start Instances Lambda Function
 * Set the region where your EC2 instances are located.
 * Set the Auto Scaling group name.
2. Stop Instances Lambda Function
 * Set the region where your EC2 instances are located.
 * Set the Auto Scaling group name.

## Deployment
1. Create the Lambda functions using the AWS Management Console or AWS CLI with the provided source code.

2. Configure the event triggers for the Lambda functions to specify when they should be invoked. For example, you can use EventBridge rules or CloudWatch Events to trigger the functions at specific times.

3. Test the functions by invoking them manually or triggering them according to your configured event triggers.

4. Monitor the function execution logs in the AWS CloudWatch Logs to ensure they are running successfully and to troubleshoot any issues if needed.

## Customization
Feel free to customize the Lambda functions based on your specific requirements. You can add additional logic, error handling, or integrate with other AWS services as needed.
