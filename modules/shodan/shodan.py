#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from requests.utils import requote_uri

from utils.send_request import send_request


def manage_response (data):
    results = None
    ip = None
    try:
        ip = str(data['ip_str'])
        print ("IP:"+ str(ip))
    except:
        print ("Not found information of the IP")
        results = ""

    finally:
        return ip


def shodan (target,api):
    r = None
    results = []
    try:
        print("[*] Starting Shodan...\n")
        for query in target:
            print ("[*]Target: " + str(query))
            url = ("https://api.shodan.io/shodan/query/search?query="+query+"?key="+api)
            url = requote_uri(url)
            print(url)
            #Sent request
            r = send_request(url)
            sleep(1)
            # Manage the response
            result = manage_response(r)
            results.append(str(ip))

    except Exception as e:
        print ("Error in shodan function" + str(e))
    finally:
        return results