# passiveapi
Tool to make a queries through the API of Censys.com, Spyse.com and BinardyEdge.io

Install the dependencies via pip:

<pre> pip3 install -r requirements.txt </pre>
  
# Usage
 
python passivequery.py -i query.txt -a apikeys.json -o output.txt 
  
You need to insert your own API KEYS in the api.json.
 
<pre>
python3 passivequery.py -h
Example of usage: python passivequery.py -i query.txt -a apikeys.json -o output.txt 

Tool to make a port scan through the API of Shodan, Censys, Onyphe and Binardy Edge

optional arguments:
  -h, --help            show this help message and exit
  -o output
                        File in txt format which will contain the ips corresponding to query
  -i INPUT, --input INPUT
                        Input Queries separated by newline
  -a apikeys, --api apikeys     Input in json with the API key of the services. Please, read the example file
</pre>

How to run with docker:
<pre>
docker build -t passivequery .
docker run -v /Users/mac/Public/configkuber:/config passivequery python3 passivequery.py -i /config/queries.txt -o /config/out.txt -a /config/ipscanapikeys.json
</pre>

Example queries: "domain.com" or "nginx", etc

Just a quick getaway for parsing IPs behind cloudflare/vulnerable servers/etc
