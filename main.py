#!/usr/bin/env python3
import os
import time

from xbot.tweetbot import Tweetbot
from xbot.confing import config


def main():
    isprofile = os.path.isdir(os.path.join(os.getcwd(), "profile"))
    bot = Tweetbot(
        config["EMAIL"], config["PASSWORD"], config["USERNAME"], config["USER_AGENT"]
    )
    if not isprofile:
        bot.login()
    bot.update_status("これはテスト投稿です。")
    time.sleep(10)
    bot.update_status_with_media("これは画像付きテスト投稿です。", ["test.jpg"])


if __name__ == "__main__":
    main()
