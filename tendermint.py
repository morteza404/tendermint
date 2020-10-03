import requests
import base58
import json

with open("/home/shahbazi/Desktop/object.builder","rb") as file:
    s = file.read()
    # print(s)

# with open("/home/shahbazi/Desktop/test2.txt","wb") as file:
#     file.write(s)



# f = bytes.fromhex("s").decode('utf-8')

# print(f)

k5 = "file7"

v5 = base58.b58encode(s)

# k6 = "name7"
# v6 = "satoshi7"

##### get stats for grafana #####
# res = requests.get('http://172.17.0.2:26660')
# print(res.text)



##### send trx #####
# res = requests.get(f'http://172.17.0.2:26657/broadcast_tx_commit?tx="{k6}={v6}"')
# print(res.text)

##### get value #####
res = requests.get(f'http://172.17.0.2:26657/abci_query?data="{k5}"')
# print(res.text)

##### send binary file as trx #####
# res = requests.get(f'http://172.17.0.2:26657/broadcast_tx_commit?tx="{k5}={v5}"')
# print(res.text)

# print(base58.b58encode(s))

dd = json.loads(res.text)["result"]["response"]["value"]

# print(dd)

print(base58.b58decode_check(dd))



