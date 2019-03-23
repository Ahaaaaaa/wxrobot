#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import post
import time
import numpy


def login(punchType):
    base_url = "https://core-std.zuolin.com"
    timestamp = time.time()

    login_payload = {
        "appKey": "bf925ea0-a5e0-11e4-a67c-00163e024631",
        "deviceIdentifier": "af59d72ad0a953c3c7560081bbe5bab516435b0a057676feff5c7d87117612b4",
        "namespaceId": 2,
        "nonce": 68848,
        "password": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
        "pusherIdentify": "appstore",
        "signature": "JXY6R6vHERg5RS2rrUXZIKI5OEU=",
        "timestamp": timestamp,
        "userIdentifier": 18698664067
    }

    punch_payload = {
        "appKey": "bf925ea0-a5e0-11e4-a67c-00163e024631",
        "createType": 0,
        "enterpriseId": 1023080,
        "identification": "75d76a08fd6fd631fd5df1ba9ec2e421",
        "latitude": 22.55072792883495,
        "longitude": 113.9525176601501,
        "nonce": 78797,
        "punchType": punchType,
        "signature": "d4KuTNH+I9qyJaPYMs2ycn+Pfnc=",
        "timestamp": timestamp,
        "wifiMac": "f0:9f:c2:f2:02:cc"
    }

    login_res = post(url=base_url + '/evh/user/logon', data=login_payload)

    if login_res.json()['errorCode'] == 200:
        token = login_res.json()['response']['loginToken']
        # return '登录成功'
        print(punch_payload)
        punch_res = post(
            url=base_url + '/evh/techpark/punch/punchClock',
            data=punch_payload,
            cookies={"token": token},
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "x-everhomes-device": "AAA470E3BBCF47C7A773B307E44E87B7-101",
                "User-Agent": "iOS/5.10.0 ns/2",
                "Accept-Language": "en-CN;q=1, zh-Hans-CN;q=0.9"
            }
        )
        print(punch_res.text)
        if punch_res.json()['errorCode'] == 200:
            if punchType == 6:
                print('签到成功')
                return '签到成功'
            if punchType == 7:
                print('签退成功')
                return '签退成功'
            if punchType == 0:
                print('上班打卡成功')
                return '上班打卡成功'
            if punchType == 1:
                print('下班打卡成功')
                return '下班打卡成功'
        else:
            if punchType == 6:
                print('签到失败')
                return '签到失败'
            if punchType == 7:
                print('签退失败')
                return '签退失败'
            if punchType == 0:
                print('上班打卡失败')
                return '上班打卡失败'
            if punchType == 1:
                print('下班打卡失败')
                return '下班打卡失败'
    else:
        return '登录失败：', login_res.text
