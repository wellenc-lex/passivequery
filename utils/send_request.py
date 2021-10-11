#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

def send_request (url):
    try:
        response = ""
        response = requests.get(url,timeout=25,allow_redirects =True)
        print(response)

    except Exception as e:
        print (e)
        response = exit(1)

    finally:
        return response.json()
