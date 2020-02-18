from instabot import Bot
from datetime import datetime
import csv
import threading   
import time
from pytz import timezone
bot = Bot()
bot.login(username="_compiler._", password="******")
def foo1():
    if int((datetime.now().astimezone(timezone('Asia/Kolkata'))).strftime("%M"))==00:#check for minute is equals 00 or not. 
        account=bot.get_user_info(bot.user_id)
        following=account['following_count']
        followers=account['follower_count']
        likes=0
        comments=0
        posts=bot.get_total_user_medias(bot.user_id)
        total_medias=len(posts)
        d_t=int(datetime.timestamp(datetime.now().astimezone(timezone('Asia/Kolkata'))))
        for post in posts:
            time.sleep(5.0)
            media_info=bot.get_media_info(post.split('_')[0])
            for count in media_info:
                likes+=count['like_count']
                comments+=count['comment_count']
        row=[d_t,total_medias,followers,following,likes,comments]
        print(row)
        with open("profile.csv","a",newline='') as csvFile:
            Fileout = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)
            Fileout.writerow(row)
        csvFile.close()
        time.sleep(60.0)
    timer1 = threading.Timer(3000.0, foo1) #50 mi sleep timer
    timer1.start()
foo1()
