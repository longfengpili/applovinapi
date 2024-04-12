# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-12 11:15:17
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 15:01:50
# @github: https://github.com/longfengpili


from pathlib import Path

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

    def get_params(self, date: str, application: str, platform: str = 'android', **kwargs):
        params = {
            'date': date,
            'application': application,
            'platform': platform,
            'api_key': self.apikey,
            'aggregated': self.aggregated,
        }
        kwargs.update(params)
        return kwargs

    def get_user_ad_info(self, date: str, application: str, platform: str = 'android', **kwargs):
        params = self.get_params(date, application, platform, **kwargs)
        res = self.request_api(self.url, params=params)
        return res

    def download_data(self, date: str, application: str, platform: str = 'android', dpath: str = None, **kwargs):
        res = self.get_user_ad_info(date, application, platform, **kwargs)
        url = res.get('ad_revenue_report_url')

        dfile = f"{application}_{platform}_{date}.csv"
        dfile = Path(dpath, dfile) if dpath else Path(dfile)
        self.download_data_to_file(url, dfile)
