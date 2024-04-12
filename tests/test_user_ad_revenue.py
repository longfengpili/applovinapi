# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-11 18:38:57
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 12:09:44
# @github: https://github.com/longfengpili

import os
import pytest

from applovin.apis import UserAdRevnueAPI

# 如果需要日期，请打开
# from pydbapi.conf.logconf import LOGGING_CONFIG
# import logging.config
# logging.config.dictConfig(LOGGING_CONFIG)


class TestAdRevnue:

    def setup_method(self, method):
        self.apikey = os.getenv('APIKEY')

    def teardown_method(self, method):
        pass

    def test_user_ad_revenue(self):
        date = '2024-04-08'
        application = 'com.st.dragoncubs.google'
        arapi = UserAdRevnueAPI(apikey=self.apikey)
        res = arapi.get_user_ad_info(application, date)
        print(res)

    def test_duser_ad_revenue(self):
        date = '2024-04-08'
        application = 'com.st.dragoncubs.google'
        arapi = UserAdRevnueAPI(apikey=self.apikey)
        res = arapi.get_user_ad_info(application, date)
        url = res.get('ad_revenue_report_url')
        arapi.download_user_ad_info(