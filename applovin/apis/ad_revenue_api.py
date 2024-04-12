# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-11 18:26:47
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 10:52:17
# @github: https://github.com/longfengpili

from applovin.utils.brequests import BRequests


class AdRevnueAPI(BRequests):
    '''https://dash.applovin.com/documentation/mediation/reporting-api/max-ad-revenue'''

    def __init__(self, apikey: str, resformat: str = 'json'):
        self.apikey = apikey
        self.resformat = resformat
        self.not_zero = 1
        super(AdRevnueAPI, self).__init__()

    @property
    def url(self):
        url = 'https://r.applovin.com/maxReport'
        return url

    @property
    def bcolumns(self):
        bcolumns = 'day,hour,store_id,package_name,application,platform,country,device_type,custom_network_name,ad_format,ad_unit_waterfall_name,has_idfa,max_ad_unit,max_ad_unit_id,max_ad_unit_test'  # noqa: E501
        return bcolumns

    def columns(self, datatype: str = 'network'):
        bcolumns = self.bcolumns
        if datatype == 'network':
            # 去掉max_placement, max_placement不支持attempts,responses,fill_rate
            columns = f'{bcolumns},network,network_placement,attempts,responses,fill_rate,impressions,ecpm,estimated_revenue'
        elif datatype == 'max':
            # 保留max_placement，删除attempts,responses,fill_rate
            columns = f'{bcolumns},network,network_placement,max_placement,impressions,ecpm,estimated_revenue'
        elif datatype == 'requests':
            # 保留requests, requests不支持network,network_palcement,max_placement
            # attempts,responses,fill_rate必须要包含network or network_palcement
            columns = f'{bcolumns},requests,impressions,ecpm,estimated_revenue'
        else:
            raise ValueError('Only supported datatype: network, max, requests')
        return columns

    def get_params(self, start: str, end: str, datatype: str = 'network', **kwargs):
        columns = self.columns(datatype)
        params = {
            'start': start,
            'end': end,
            'columns': columns,
            'api_key': self.apikey,
            'format': self.resformat,
            'not_zero': self.not_zero
        }
        kwargs.update(params)
        return kwargs

    def get_ad_revenue(self, start: str, end: str, datatype: str = 'network', **kwargs):
        params = self.get_params(start, end, datatype, **kwargs)
        res = self.request_api(self.url, params=params)
        return res
