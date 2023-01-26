import requests
import time
import random
import string 

from fake_useragent import UserAgent

import random

c = 0

with open("twitter.txt") as file1, open("wallet.txt") as file3:
    for twitter, wallet in zip(file1, file3):
        c = c + 1
        ua = UserAgent()
        useragent = ua.random
        s = 22
        ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))    
        link = "https://twitter.com/BunniesInChina/status/1618141806939738112?s=20&t=" + str(ran)

        headers = { 

        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8",
        "content-type": "application/json",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "referrer": "https://bunniesinchina.com/",
        "body": '"{\"twitter\":\"' + twitter.rstrip() + '\",\"retweet\":\"' + link + '\",\"wallet\":\"' + wallet.rstrip() + '\",\"code\":\"YbUpsqcj\"}"',
        "referrerPolicy": "strict-origin-when-cross-origin"
        }
        url = "https://adegen.onrender.com/task"
        request = requests.post(url=url, headers=headers)
        print(str(request.status_code) + " : " + str(c) + " : " + twitter.rstrip() + " : " + wallet.rstrip())
        time.sleep(1)
