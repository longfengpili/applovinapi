# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2023-07-17 17:12:49
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-04-11 19:03:31

import requests

import logging
brequestlogger = logging.getLogger(__name__)


class BRequests:

    def __init__(self):
        pass

    def request_api(self, url: str, params: dict, retries: int = 3):
        attempt = 0
        while attempt < retries:
            response = requests.get(url, params=params)
            if response.status_code in (200, 204):
                break

            attempt += 1
            brequestlogger.error(f"[get] {url}, Attempt {attempt}, status_code: {response.status_code}")

        result = response.json()
        return result