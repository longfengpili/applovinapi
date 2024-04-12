# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-12 11:15:17
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 12:09:20
# @github: https://github.com/longfengpili


from .base_api import BaseAPI


class UserAdRevnueAPI(BaseAPI):
    '''https://dash.applovin.com/documentation/mediation/reporting-api/user-ad-revenue'''

    def __init__(self, apikey: str):
        self.aggregated = 'false'
        super(UserAdRevnueAPI, self).__init__(apikey)

    @property
    def url(self):
        url = 'https://r.applovin.com/max/userAdRevenueReport'
        return url

    def columns(self):
        pass

    def get_params(self, application: str, date: str, platform: str = 'android', **kwargs):
        params = {
            'date': date,
            'application': application,
            'platform': platform,
            'api_key': self.apikey,
            'aggregated': self.aggregated,
        }
        kwargs.update(params)
        return kwargs

    def get_user_ad_info(self, application: str, date: str, **kwargs):
        params = self.get_params(application, date, **kwargs)
        res = self.request_api(self.url, params=params)
        return res

    def download_user_ad_info(self, url: str, dfile: str):
        res = self.request_api(url, restype='content')
        with open(dfile, 'wb') as f:
            f.write(res)
