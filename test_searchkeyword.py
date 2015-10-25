#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import ConfigParser

from searchkeyword import SearchKeyword

def main():

    inifile = ConfigParser.SafeConfigParser()
    inifile.read("./config.ini")

    for tweet in SearchKeyword(
        inifile.get('twitter_api', 'consumer_key'),
        inifile.get('twitter_api', 'consumer_secret'),
        inifile.get('twitter_api', 'access_token'),
        inifile.get('twitter_api', 'access_token_secret'),
        inifile.get('search', 'keyword'),
        long(inifile.get('search', 'last_tweet_id')),
        int(inifile.get('search', 'max_tweet'))):

        print('==========================================================')
        print( "screen_name: {0}".format( tweet['screen_name']) )
        print( u"user_name: {0}".format( tweet['user_name'] ) )
        print( u"text: {0}".format( tweet['text'] ) )
        print( "profile_image_url: {0}".format( tweet['profile_image_url']) )
        print( "created_at: {0}".format( tweet['created_at']) )
        print( "id: {0}".format( tweet['id'] ) )

if __name__ == '__main__':
    sys.exit(main())
