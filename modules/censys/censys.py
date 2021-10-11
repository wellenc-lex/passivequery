#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from requests.utils import requote_uri

from censys.search import CensysHosts
ips =[]

def censys (target, secret, uid):
    global ips
    try:
        print ("\n[*] Starting censys...\n")
        for query in target:
            print ("[*]Target:" + str(query))
            h = CensysHosts(api_secret=secret, api_id=uid)
            
            for page in h.search(query, pages=10):
                print(page)
                
                try:
                    for results in page:
                        print(results["ip"])
                        ips.append(results["ip"])

                except Exception as exc:
                    print ("Error in for each page function " + str(exc))
                    pass
                    
            print(ips)

    except Exception as exc:
        print ("Error in censys function " + str(exc))
        pass
    finally:
        return ips
