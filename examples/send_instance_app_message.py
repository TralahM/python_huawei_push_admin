﻿# -*-coding:utf-8-*-
#
# Copyright 2020. Huawei Technologies Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

import push_admin
from push_admin import messaging

android = messaging.AndroidConfig(
    collapse_key=-1,
    urgency=messaging.AndroidConfig.HIGH_PRIORITY,
    ttl="10000s",
    bi_tag="the_sample_bi_tag_for_receipt_service",
    fast_app_target=1,
    category=None,
)


def send_push_android_data_message():
    """
    a sample to show hwo to send web push message
    :return:
    """
    message = messaging.Message(
        # English sample
        # data = "{\"pushtype\":0,\"pushbody\":{\"title\":\"Welcome to use Huawei HMS Push Kit?\",\"description\":\"One "
        #       + "of the best push platform on the planet!!!\",\"page\":\"/\",\"params\":{\"key1\":\"test1\",\"key2\":\"test2\"},\"ringtone\":"
        #       + "{\"vibration\":\"true\",\"breathLight\":\"true\"}}}",
        # Chinese sample
        data='{"pushtype":0,"pushbody":{"title":"欢迎使用华为HMS Push Kit！","description":"世界上最好，'
        + '最优秀的推送平台！！！","page":"/","params":{"key1":"test1","key2":"test2"},"ringtone":'
        + '{"vibration":"true","breathLight":"true"}}}',
        android=android,
        # TODO
        token=["your token"],
    )

    try:
        # Case 1: Local CA sample code
        # response = messaging.send_message(message, verify_peer="../Push-CA-Root.pem")
        # Case 2: No verification of HTTPS's certificate
        response = messaging.send_message(message)
        # Case 3: use certifi Library
        # import certifi
        # response = messaging.send_message(message, verify_peer=certifi.where())
        print("response is ", json.dumps(vars(response)))
        assert response.code == "80000000"
    except Exception as e:
        print(repr(e))


def init_app():
    """init sdk app"""
    # TODO
    app_id = "Your instance application's (not android app) app id"
    app_secret = "Your instance application's (not android app)  app secret"
    push_admin.initialize_app(app_id, app_secret)


def main():
    init_app()
    send_push_android_data_message()


if __name__ == "__main__":
    main()
