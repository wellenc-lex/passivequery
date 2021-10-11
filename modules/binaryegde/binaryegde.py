#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
import requests
import json
from requests.utils import requote_uri

ips = []

flag = 0

def manage_response(data):
    global ips
    global flag
    try:
        if data['events'] == []: 
                flag = 1

        for result in data['events']:
            print("ips: " + str(result['ip']))
            ips.append(str(result['ip']))

    except Exception as exc:
        print("Error in manage_response " + str(exc))
        flag = 1
        return flag

    finally:
        return (data["total"]/20)

def send_request(url, api, page):
    global flag
    response = ""
    api_key = {'X-Key': api}
    flag = 0  # 0 = 200, 1=404
    try:
        response = requests.get(url+"&page="+str(page), timeout=15, allow_redirects=True, headers=api_key)
        print(url+"&page="+str(page))
        if response.status_code == 404:
            print("Not found information of the query, pass the next")
            flag = 1
    except Exception as exc:
        response = ""
        print("Error in send_request" + str(exc))
    finally:
        return response.json()


def binaryegede (target,api):
    global flag

    r = None
    try:
        print("\n[*] Starting BinaryEgede...\n")
        for query in target:
            page = 0
            flag = 0

            print ("[*]Query: " + str(query))
            query = requote_uri(str(query))
            url ="https://api.binaryedge.io/v2/query/search?query="+query+"&only_ips=1".format(query)
            
            while (flag!=1):
                page+=1
                (r) = send_request(url,api, page)
                manage_response(r)
                sleep(1)

    except Exception as exc:
        print ("Error in main function " + str(exc))

    finally:
        return ips
