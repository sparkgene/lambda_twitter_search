#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import ConfigParser

from slackclient import SlackClient

def main():

    inifile = ConfigParser.SafeConfigParser()
    inifile.read("./config.ini")

    attachments = [
        {
            "fallback": "summury of post",
            "pretext": "https://twitter.com/",
            "author_name": "lambda twitter search",
            "author_link": "https://github.com/sparkgene/lambda_twitter_search",
            "author_icon": "https://pbs.twimg.com/profile_images/378800000804318231/391afeb31a92d3782f0e39a71113355e_400x400.png",
            "text": "test tweet contents",
            "color": "#439FE0"
        }
    ]

    sc = SlackClient(inifile.get('slack', 'token'))
    sc.api_call("chat.postMessage",
                channel=inifile.get('slack', 'channel'),
                attachments=json.dumps(attachments),
                username=inifile.get('slack', 'username'),
                icon_emoji=inifile.get('slack', 'icon_emoji'))

if __name__ == '__main__':
    sys.exit(main())
