#!/usr/bin/python
# -*- coding: utf-8 -*-

import werobot
import re
import json
from requests import post
from punchClock import login
from tuling import tuling

robot = werobot.WeRoBot(token='wangbin')


@robot.text
def hello(message):
    if re.compile("^爱我[吗么]$").match(message.content):
        return "我爱Holly呀"
    if message.source == "o6Xocs9z1zngjVbn8WZVmlmV1Ukk":
        if message.content == "上班":
            return login(0)
        if message.content == "下班":
            return login(1)
        if message.content == "签退":
            return login(7)
        if message.content == "签到":
            return login(6)
    return tuling(text=message.content)


@robot.subscribe
def subscribe():
    return \
        "喵喵喵～～\n" \
        "问问小哈酱天气呀？\n" \
        "问问小哈酱喜不喜欢你呀～"


@robot.voice
def voice(message):
    return tuling(message.recognition)


@robot.image
def image():
    return "image"


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8080
# robot.run()

# if app