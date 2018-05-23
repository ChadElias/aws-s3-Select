import boto3
import json
import os
import sys
from dateutil.parser import parse

s3 = boto3.client('s3', region_name='us-west-2')

def lambda_handler(event, context):

    bucketName = os.environ['BUCKET_NAME']
    records = []

    paginator = s3.get_paginator('list_objects_v2')
    result = paginator.paginate(Bucket=bucketName)

    for page in result:
        if 'Contents' in page:
            for key in page['Contents']:
                bucketKey = key['Key']

                try:
                    queryResponse = s3.select_object_content(
                        Bucket=bucketName,
                        Key=bucketKey,
                        ExpressionType='SQL',
                        Expression="select s.\"FirstName\", s.\"LastName\", s.\"Class\", s.\"TimeStamp\"  from s3object s",
                        InputSerialization={'JSON': {"Type": "Lines"}},
                        OutputSerialization={'JSON': {}}
                    )
                except:
                    print('ERROR - Exception performing S3 Select on Key: ' + bucketKey + '. Message: ' + sys.exc_info()[0])

                for responses in queryResponse['Payload']:
                        if 'Records' in responses:
                            try:
                                getJson = json.loads(responses['Records']['Payload'])
                                parsedTime = parse(getJson['TimeStamp'])
                                getJson['TimeStamp'] = str(parsedTime.month) + '/' + str(parsedTime.day) + '/' + str(parsedTime.year)
                                records.append(getJson)
                            except:
                                print('ERROR - Exception performing JSON to Python Object on Key: ' + bucketKey + '. Message: ' + sys.exc_info()[0])
                
        else:
            print('ERROR - Bucket: ' + bucketName + ' did not contain any keys!')
    
    return records