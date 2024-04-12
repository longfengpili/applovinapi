# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-11 18:26:47
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 15:26:55
# @github: https://github.com/longfengpili

import json
from pathlib import Path

from .base_api import BaseAPI


class AdRevnueAPI(BaseAPI):
    '''https://dash.applovin.com/documentation/mediation/reporting-api/max-ad-revenue'''

    def __init__(self, apikey: str, resformat: str = 'json'):
        self.resformat = resformat
        self.not_zero = 1
        super(AdRevnueAPI, self).__init__(apikey)

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

    def download_data(self, start: str, end: str, datatype: str = 'network', dpath: str = None, **kwargs):
        res = self.get_ad_revenue(start, end, datatype, **kwargs)
        res = res.get('results')
        res = '\n'.join([json.dumps(i, ensure_ascii=False) for i in res])

        dfile = f"ad_revenue_{start}_{end}.csv"
        dfile = Path(dpath, 'ad_revnue', dfile) if dpath else Path('ad_revnue', dfile)

        dpath = dfile.resolve().parent
        if not dpath.exists():
            dpath.mkdir(parents=True)
        
        with dfile.open('w', encoding='utf-8') as f:
            f.write(res)
