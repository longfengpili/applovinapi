# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-04-11 18:26:47
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 17:16:48
# @github: https://github.com/longfengpili

import json
from pathlib import Path

from .base_api import BaseAPI


class DirectSoldAPI(BaseAPI):
    '''https://dash.applovin.com/documentation/mediation/reporting-api/direct-sold'''

    def __init__(self, apikey: str, resformat: str = 'json'):
        self.resformat = resformat
        super(DirectSoldAPI, self).__init__(apikey)

    @property
    def url(self):
        url = 'https://r.applovin.com/maxDirectSoldReport'
        return url

    @property
    def columns(self):
        columns = 'day,store_id,package_name,application,platform,country,device_type,campaign,campaign_id,creative,creative_id,order,order_id,ad_format,ad_unit_waterfall_name,has_idfa,max_ad_unit,max_ad_unit_id,max_ad_unit_test,cost,impressions,clicks,ctr'  # noqa: E501
        return columns

    def get_params(self, start: str, end: str, **kwargs):
        columns = self.columns
        params = {
            'start': start,
            'end': end,
            'columns': columns,
            'api_key': self.apikey,
            'format': self.resformat
        }
        kwargs.update(params)
        return kwargs

    def get_direct_sold(self, start: str, end: str, **kwargs):
        params = self.get_params(start, end, **kwargs)
        print(params)
        res = self.request_api(self.url, params=params)
        return res

    def download_data(self, start: str, end: str, dpath: str = None, **kwargs):
        res = self.get_direct_sold(start, end, **kwargs)
        res = res.get('results')
        res = '\n'.join([json.dumps(i, ensure_ascii=False) for i in res])

        dfile = f"ad_revenue_{start}_{end}.csv"
        dfile = Path(dpath, 'ad_revnue', dfile) if dpath else Path('ad_revnue', dfile)

        dpath = dfile.resolve().parent
        if not dpath.exists():
            dpath.mkdir(parents=True)
        
        with dfile.open('w', encoding='utf-8') as f:
            f.write(res)
