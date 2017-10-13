#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wxpy import *

if __name__ == "__main__":
    bot = Bot()
    my_friend = bot.friends().search('大')[0]
    print(my_friend)
    tuling = Tuling(api_key = 'ea8e0c5954924497a9261defc31f31d8')
    @bot.register(my_friend)
    def reply_my_friend(msg):
        tuling.do_reply(msg)
    bot.join()
