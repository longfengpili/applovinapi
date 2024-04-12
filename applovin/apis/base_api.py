# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-11 18:26:47
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 15:06:04
# @github: https://github.com/longfengpili

from abc import ABCMeta, abstractmethod

from applovin.utils.brequests import BRequests


class BaseAPI(BRequests, metaclass=ABCMeta):

    def __init__(self, apikey: str):
        self.apikey = apikey
        super(BaseAPI, self).__init__()

    @property
    @abstractmethod
    def url(self):
        pass

    @abstractmethod
    def columns(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @abstractmethod
    def download_data(self):
        pass
