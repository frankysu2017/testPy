#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wxpy import *

bot = Bot(cache_path = True)
bot.enable_puid()
my_friends = bot.friends()
#for friend in my_friends:
#    print(friend)
print(my_friends.stats_text())
prov_stat = dict(my_friends.stats()['province'])
prov_stat= dict(sorted(prov_stat.items(), key = lambda d:d[1], reverse = True))
for item in prov_stat.keys():
    if item == '':
        item = None
f_in_p = [bot.friends().search(province = item) for item in prov_stat.keys()]
print(bot.chats()[1].get_avatar())
#以下是自动回复的原始代码
my_friend = bot.friends().search("王文婷")[0]
#my_friend.send_image(r'C:\Users\WEB_PC_X1\Pictures\Camera Roll\botstart.png')
@bot.register(my_friend)
def reply_my_friend(msg):
    print(msg)
    print(tuling.do_reply(msg))


if __name__ == "__main__":
    tuling = Tuling(api_key='ea8e0c5954924497a9261defc31f31d8')

    bot.join()