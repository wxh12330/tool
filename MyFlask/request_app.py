#coding = utf-8


# import requests
#
# if __name__ == '__main__':
#     r = requests.post("http://127.0.0.1:5000/data_request/222", data="12893")
#     print(r.json())
#     print(r.headers)
#     print(r.reason)

from suds.client import Client as SudsClient
import requests

url = 'http://127.0.0.1:50001/hello?wsdl'
client = SudsClient(url=url, cache=None)
r = client.service.hello('hello world', 1)
print(r)
