import requests
from time import sleep
from requests.utils import requote_uri

ips = []

def send_request(query, apikey, offset):
    try:
        global ips

        pages = ""

        url = "https://api.spyse.com/v4/data/ip/search"

        payload = {"limit":100,"offset":offset,"query": query }

        #print(payload)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(apikey)
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        json = response.json()

        pages = json["data"]["total_items"]

        for i in json["data"]["items"]:
            ips.append(i["ip"])

    except Exception as exc:
        print("Error in send_request" + str(exc))
        pass
    finally:
        return pages

def spyse(query, apikey):
    try:
        global ips
        query = requote_uri(str(query))
        pages = send_request(query, apikey, 0)
        sleep(2)

        i=100
        while i<pages:
            send_request(query, apikey, i)
            i += 100
            sleep(2)
        #print(ips)

    except Exception as e:
        print ("Error in spyse function" + str(e))
    finally:
        return ips