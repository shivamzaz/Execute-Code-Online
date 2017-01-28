import requests
RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
CLIENT_SECRET = 'b7c7f5f82184067e05545fc010bb9475fb37217c'
inp=raw_input()
#input=inp+".txt"
source=open(inp,"r").read()
data = {
	'client_secret': CLIENT_SECRET,
	'async': 0,
	'source': source,
	'lang': "PYTHON",
	'time_limit': 5,
	'memory_limit': 262144,
	}
r = requests.post(RUN_URL, data=data)
print r.json()
