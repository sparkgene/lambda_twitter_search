# -*- coding: utf-8 -*-
import boto3
import json
import ConfigParser

from searchkeyword import SearchKeyword
from slackclient import SlackClient

print('Loading function')

def lambda_handler(event, context):

    inifile = ConfigParser.SafeConfigParser()
    inifile.read("./config.ini")

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tweet_id')
    result = table.scan()
    previous_last_id = 0
    for row in result['Items']:
        if row['last_id'].isdigit():
            previous_last_id = long(row['last_id'])

    last_id = previous_last_id
    print("last_id: {0}".format(previous_last_id))

    max_send_count = inifile.get('search', 'max_tweet')
    if max_send_count.isdigit():
        max_send_count = int(max_send_count)
    send_count = 0
    for tweet in SearchKeyword(
        inifile.get('twitter_api', 'consumer_key'),
        inifile.get('twitter_api', 'consumer_secret'),
        inifile.get('twitter_api', 'access_token'),
        inifile.get('twitter_api', 'access_token_secret'),
        inifile.get('search', 'keyword'),
        previous_last_id):

        if send_count == 0:
            last_id = tweet['id']
        elif send_count > max_send_count:
            break # sending many tweets to slack takes long time.
        send_count += 1

        sc = SlackClient(inifile.get('slack', 'token'))
        attachments = [
            {
                "fallback": tweet['text'],
                "pretext": "https://twitter.com/{0}/status/{1}".format(
                    tweet['screen_name'],
                    tweet['id']
                ),
                "author_name": tweet['user_name'],
                "author_link": "https://twitter.com/{0}".format(
                    tweet['screen_name']
                ),
                "author_icon": tweet['profile_image_url'],
                "text": tweet['text'],
                "color": "#439FE0"
            }
        ]
        sc.api_call("chat.postMessage",
                channel=inifile.get('slack', 'channel'),
                attachments=json.dumps(attachments),
                username=inifile.get('slack', 'username'),
                icon_emoji=inifile.get('slack', 'icon_emoji'))


    if last_id > previous_last_id:
        table.put_item(
            Item={"last_id": last_id }
        )
