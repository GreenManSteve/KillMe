import json

import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FramScores')


class Mis(object):
    def __init__(self):
        pass

    def get_test_stats(self, gender):
        response = table.query(
            # Add the name of the index you want to use in your query.
            IndexName="sk-index",
            KeyConditionExpression=Key('sk').eq(gender),
        )
        data = json.loads(response['body'])

        count = (data['Count'])
        return count
