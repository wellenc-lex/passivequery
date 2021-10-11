# passiveapi
Tool to make a queries through the API of Shodan, Censys, Onyphe and Binardy Edge

Install the dependencies via pip:

<pre> pip3 install -r requirements.txt </pre>
  
# Usage
 
python3 heisenberg.py -q <queries.txt> -a <API.json>
  
You need update your own API KEYS in the parameter file api.json. In the repository there is a example.
 
<pre>
python3 heisenberg.py -h
usage: heisenberg.py [-h] [-e EXPORT] -i INPUT -a API

Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge

optional arguments:
  -h, --help            show this help message and exit
  -e EXPORT, --export EXPORT
                        File in txt format which contains the ips corresponding to query
  -i INPUT, --input INPUT
                        Input in txt with the Queries
  -a API, --api API     Input in json with the API key of the services. Please, read the example file
</pre>
  
# Dependencies

Dependencies in python3:

<pre>
  requests
  json
</pre>