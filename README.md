# lambda_twitter_search
AWS Lambda function for search tweets with keyword and post to slack.

## Overview

This is a Scheduled Lambda function for search keyword from twitter and post to slack.
The function use DynamoDB to store last tweet id.(setting up DynamoDB is required. DynamoDB and Lambda function must located on same region)

![slack post image](https://raw.githubusercontent.com/sparkgene/lambda_twitter_search/master/slack_post_image.png)

## Installation

```
git clone https://github.com/sparkgene/lambda_twitter_search
pip install -r requirements.txt -t /path/to/lambda_twitter_search
```

## Configuration

```
cp lambda_twitter_search/config.ini.org lambda_twitter_search/config.ini
```

Edit `config.ini` with editor and fill up the settings.

```
[twitter_api]
consumer_key        = # your twitter application consumer_key
consumer_secret     = # your twitter application consumer_secret
access_token        = # your twitter application access_token
access_token_secret = # your twitter application access_token_secret

[search]
keyword = # the key word you want to search
max_tweet = # If the keyword found in many tweets, slack post explodes and lambda will time out. So few tweets is good for using.

[slack]
token = # slack api token
username = py_bot # name shown on slack message
channel = # tweet post channel
icon_url = # costom icon for slack message
icon_emoji = :slack: # use icon. this overrides icon_url.

[dynamodb]
table_id = lambda_ids
id_value = 1
source = lambda_twitter_search
```

### twitter_api section

Use your twitter app keys.
https://apps.twitter.com/

### search section
Set the keyword which you want to search.

ex)

```
keyword = lambda
```

### slack section

Create a api token. https://api.slack.com/web
Other keys are based on https://api.slack.com/methods/chat.postMessage
If post do not appear to your channel, set `channel id` to `channel`.

### dynamodb section

This schema is same with [lambda_review_checker](https://github.com/sparkgene/lambda_review_checker).
If you use both lambda function, change the `id_value` to be unique.

## Testing config.ini

Test the slack configuration with following command.

``` shell
python test_slack.py
```

Test the twitter search configuration with following command.

``` shell
python test_searchkeyword.py
```

## Usage

1. Edit config.ini
2. Create Amazon DynamoDB table.

  ``` shell
  # create table
  aws dynamodb create-table --table-name lambda_ids --attribute-definitions AttributeName=Id,AttributeType=N --key-schema AttributeName=Id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

  # insert default value
  aws dynamodb put-item --table-name lambda_ids --item '{"Id":{"N":"1"},"LastId":{"N":"0"}, "source": {"S":"lambda_twitter_search"}}'

  # confirm data is insert correct.
  aws dynamodb get-item --table-name lambda_ids --key '{"Id":{"N":"1"}}'
  ```
3. Pack function

  ``` shell
  zip -r func.zip . -x .git/**/*
  ```
  details
  http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
4. Upload to your lambda function
  See details createing scheduled lambda function.
  http://docs.aws.amazon.com/lambda/latest/dg/getting-started-scheduled-events.html

## Caution

Using this scripts on AWS is not free.

[Amazon DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/)

[AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/)
