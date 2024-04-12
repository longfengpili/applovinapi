# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2023-07-17 17:12:49
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-12 15:28:06

from pathlib import Path
import requests

import logging
brequestlogger = logging.getLogger(__name__)


class BRequests:

    def __init__(self):
        pass

    def request_api(self, url: str, params: dict = None, retries: int = 3, restype: str = 'text'):
        attempt = 0
        while attempt < retries:
            response = requests.get(url, params=params)
            if response.status_code in (200, 204):
                break

            attempt += 1
            brequestlogger.error(f"[get] {url}, Attempt {attempt}, status_code: {response.status_code}")

        try:
            result = response.json()
        except:  # noqa: E722
            result = response.text if restype == 'text' else response.content
        return result

    def download_url_to_file(self, url: str, dfile: str):
        res = self.request_api(url, restype='content')
        dfile = Path(dfile)
        dpath = dfile.resolve().parent
        if not dpath.exists():
            dpath.mkdir(parents=True)
            
        with dfile.open('wb') as f:
            f.write(res)
