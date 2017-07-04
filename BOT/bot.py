# -*- coding: utf-8 -*-

from slackclient import SlackClient
import json
from SQL import sqliteWrapper


class SlackBot:
    channel = ""
    user = ""
    text = ""
    right_info = False


    def basic(self):

        print "WHAM!!!!!"
        DB = sqliteWrapper.sql().connect("nobigyul.db")

        token = "xoxb-24779113027-zeP220ZhisB30lyV1DDM1NFc"  # found at https://api.slack.com/web#authentication
        sc = SlackClient(token)

        bot_status = ""

        if sc.rtm_connect():

            bot_status = "ALIVE"

            while True:
                # print sc.rtm_read()
                message = json.dumps(sc.rtm_read(), ensure_ascii=False)

                if len(message) != 2:  # 아무것도 없는 메세지 일때대
                    print message
                # time.sleep(1)

                json_data = json.loads(message)

                if len(json_data) == 1:
                    if 'channel' in json_data[0]:
                        channel = json_data[0]['channel']
                    if 'user' in json_data[0]:
                        user = json_data[0]['user']
                    if 'text' in json_data[0]:
                        text = json_data[0]['text']
                        if text.encode('utf8') == "잘자":
                            bot_status = "DEAD"
                            sc.api_call("chat.postMessage", as_user="true", channel=str(channel), text="그럼 수고해~")
                        elif text.encode('utf8') == "일어나" and user != "":
                            bot_status = "ALIVE"
                            sc.api_call("chat.postMessage", as_user="true", channel=str(channel), text="하암~ 잘잤다!")

                    if 'user' in json_data[0]:
                        if user == "U04FKQBU1" and bot_status == "ALIVE":
                            sc.api_call("chat.postMessage", as_user="true", channel=str(channel), text=text)
        else:
            print "Connection Failed, invalid token?"
