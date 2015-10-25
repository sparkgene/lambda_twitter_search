# lambda_twitter_search
AWS Lambda function for search tweets with keyword and post to slack

## Work in progress

### Installation

git clone https://github.com/sparkgene/lambda_twitter_search
pip install -r requirements.txt -t /path/to/lambda_twitter_search

### Configuration

cp lambda_twitter_search/config.ini.org lambda_twitter_search/config.ini

Edit `config.ini` with editor and fill up the settings.

```
[twitter_api]
consumer_key        =
consumer_secret     =
access_token        =
access_token_secret =

[search]
keyword = python

[slack]
token =  
username = py_bot
channel =
icon_url =
icon_emoji = :slack:
```

#### twitter_api

Use your twitter app keys.
https://apps.twitter.com/

#### search
Set the keyword which you want to search.

ex)

```
keyword = lambda
```

#### slack

Create a api token. https://api.slack.com/web
Other keys are based on https://api.slack.com/methods/chat.postMessage


aws dynamodb create-table --cli-input-json file://dynamodb_table.json
