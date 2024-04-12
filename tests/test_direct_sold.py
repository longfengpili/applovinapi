# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-11 18:38:57
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 17:06:52
# @github: https://github.com/longfengpili

import os
import pytest

from applovin.apis import DirectSoldAPI

# 如果需要日期，请打开
# from pydbapi.conf.logconf import LOGGING_CONFIG
# import logging.config
# logging.config.dictConfig(LOGGING_CONFIG)


class TestDirectSold:

    def setup_method(self, method):
        self.apikey = os.getenv('APIKEY')

    def teardown_method(self, method):
        pass

    # @pytest.mark.parametrize('datatype', ['network', 'max', 'requests'])
    @pytest.mark.parametrize('datatype', ['network'])
    def test_get_direct_sold(self, datatype):
        start = '2024-04-08'
        end = '2024-04-11'
        arapi = DirectSoldAPI(apikey=self.apikey)
        res = arapi.get_direct_sold(start, end, datatype=datatype)
        print(res)

    def test_d_direct_sold(self):
        start = '2024-04-08'
        end = '2024-04-11'
        arapi = DirectSoldAPI(apikey=self.apikey)
        arapi.download_data(start, end, datatype='network', dpath='data')
