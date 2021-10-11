# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" LIBRARIES"""
import argparse
import sys
import json

from modules.binaryegde.binaryegde import binaryegede
from modules.censys.censys import censys
from modules.shodan.shodan import shodan
from modules.spyse.spyse import spyse
from utils.export_results import export_results
from utils.read_api import read_api
from utils.read_input import read_input

""" IMPORT MODULES """

def help ():
    """FUNCTION HELP"""
    print (""" \nTool to make a queries through the API of Shodan, Censys, Onyphe and Binardy Edge

        			Example of usage: python passivequery.py -i query.txt -a apikeys.json -o output.txt """)

def main (argv):
    """ FUNCTION MAIN"""
    parser = argparse.ArgumentParser(
        description="Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input', help="Txt with Queries",
                        required=True)
    parser.add_argument('-a', '--apikeys', help="API key file",
                        required=True)
    parser.add_argument('-o', '--output', help="API key file",
                        required=True)
    args = parser.parse_args()

    """ local var"""
    path = args.input # Get input file
    output = args.output #Get output
    api = args.apikeys # Get API key
    query =[] # list to save the input IP
    api_keys = []
    shodan_results = []
    censys_results = []
    onyphe_results = []
    binaryedge_results = []
    spyse_results = []

    # functions banner and help
    help()

    try:
        #Read input parameters
        query = read_input (path)
        #Read API keys
        api_keys = read_api(api)
        api_shodan = api_keys['api_shodan']
        api_censys_secret = api_keys ['censys_secret']
        api_censys_uid = api_keys['censys_uid']
        api_onyphe = api_keys ['onyphe_api']
        api_binaryegde = api_keys ['binaryedge_api']
        api_spyse = api_keys ['spyse_api']

        #call The different API's
        #Shodan
        print ("\n[*] Call Shodan: \n")
        #shodan_results = shodan(query,api_shodan) requires paid api key -> not working. also rewerite with import shodan later. waiting for 5$ action
        #print(shodan_results)

        #onyphe
        print ("\n[*] Call Onyphe: \n")
        #onyphe_results = 0#onyphe(query, api_onyphe) #60eur perpetual -> not working.
        
        #censys
        print ("\n[*] Call Censys: \n")
        censys_results = censys(query, api_censys_secret, api_censys_uid)
        print(censys_results)
        
        #spyse
        print ("\n[*] Call Spyse: \n")
        spyse_results = spyse(query, api_spyse)
        print(spyse_results)

        #BinaryEgede
        print ("\n[*] Call BinaryEgede: \n")
        binaryedge_results = binaryegede(query,api_binaryegde)
        print(binaryedge_results)

        #binaryedge_results = ['23.6.184.102', '104.97.120.133', '23.77.122.238', '104.93.73.119', '104.102.122.190', '23.8.91.31', '23.199.157.152', '104.93.179.15', '104.101.149.28', '23.13.24.131', '23.63.185.166', '23.214.25.67', '104.87.40.116', '23.212.138.34', '23.53.73.249', '23.63.133.149', '23.201.232.125', '54.225.188.155', '23.199.166.172', '104.117.202.205', '23.79.208.29', '184.85.186.224', '104.67.180.239', '23.76.135.215', '122.252.138.86', '52.78.218.229', '34.238.28.30', '104.71.119.24', '34.72.234.63', '104.108.1.224', '23.222.187.152', '23.32.210.63', '47.106.28.149', '2.20.114.147', '104.64.75.179', '104.106.209.72', '125.252.215.118', '104.76.81.46', '23.37.24.69', '104.72.120.240']
        #spyse_results = ['47.241.9.25', '94.130.151.73', '94.130.151.73', '54.92.147.117', '103.22.200.200', '182.64.41.157', '141.101.64.100', '106.212.7.230']

        export_results (query, output, shodan_results, censys_results, spyse_results, binaryedge_results)


    except Exception as exc:
        print ("Error in main funcion" + str(exc))

# CALL MAIN
if __name__ == "__main__":
   main(sys.argv[1:])