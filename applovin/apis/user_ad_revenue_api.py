# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-12 11:15:17
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 11:36:18
# @github: https://github.com/longfengpili


from .base_api import BaseAPI


class AdRevnueAPI(BaseAPI):
    '''https://dash.applovin.com/documentation/mediation/reporting-api/user-ad-revenue'''

    def __init__(self, apikey: str):
        self.aggregated = 'false'
        super(AdRevnueAPI, self).__init__(apikey)

    @property
    def url(self):
        url = 'https://r.applovin.com/max/userAdRevenueReport'
        return url

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
