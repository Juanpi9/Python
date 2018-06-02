import boto3
sns = boto3.client('sns')
phone_number='xxxxxxxxxx'
sns.publish(Message='MessageTEST',PhoneNumber=phone_number)