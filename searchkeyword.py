#!/usr/bin/python
# -*- coding: utf-8 -*-
from TwitterSearch import *

class SearchKeyword:
    """
    use twitter search api to find tweets include keyword
    """
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, keyword, since_id, tweet_count=15):
        self._results = []
        self._i = 0

        try:
            tso = TwitterSearchOrder()
            tso.set_keywords([keyword])
            tso.set_language('ja')
            tso.set_include_entities(False)
            tso.set_count(tweet_count)
            if since_id > 0:
                tso.set_since_id(since_id)

            ts = TwitterSearch(
                consumer_key = consumer_key,
                consumer_secret = consumer_secret,
                access_token = access_token,
                access_token_secret = access_token_secret
             )

            for tweet in ts.search_tweets_iterable(tso):
                self._results.append(
                    {
                        'screen_name': tweet['user']['screen_name'],
                        'user_name': tweet['user']['name'],
                        'profile_image_url': tweet['user']['profile_image_url'],
                        'text': tweet['text'],
                        'created_at': tweet['created_at'],
                        'id': tweet['id']
                    }
                )

        except TwitterSearchException as e:
            print(e)

    def __iter__(self):
        return self

    def next(self):
        if self._i == len(self._results):
            raise StopIteration()
        value = self._results[self._i]
        self._i += 1
        return value
