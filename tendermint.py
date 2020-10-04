import requests
import base58
import base64
import json

"""
    Author : Morteza Shahbazi
    Project : Simurgh
    Version : v0.1.0
    Description:
                the goal is storing ring files in kvstore.
                first we read ring file binary content and convert it to base58.
                then accoumplish transaction like this : 
                            requests.get(f'http://172.17.0.2:26657/broadcast_tx_commit?tx="{k5}={v5}"')
                after this, we get value of transaction (ring content) as base64 and decode it.
                            requests.get(f'http://172.17.0.2:26657/abci_query?data="{k5}"')
                finally convert base64 to base58 and save new ring file(s).
                enjoy :)))              

"""

# trx_key : arbitrary transaction key name
def send_transaction(trx_key, ring_file):
    with open(f"/home/shahbazi/Desktop/{ring_file}","rb") as file:
        s = file.read()
        # print(s)
    trx_value = base58.b58encode(s)
    res = requests.get(f'http://172.17.0.2:26657/broadcast_tx_commit?tx="{trx_key}={trx_value}"')
    print(res.text)

# trx_key : arbitrary transaction key name
def get_transaction_value(trx_key, new_ring_file):
    res = requests.get(f'http://172.17.0.2:26657/abci_query?data="{trx_key}"')
    # print(res.text)
    trx_value = json.loads(res.text)["result"]["response"]["value"]
    b64_value = base64.standard_b64decode(trx_value)
    b64_list = str(b64_value).split('b"b')[1].replace('"','').replace('\'','')
    b64_bytes = bytes(b64_list, 'utf-8') 
    print(base58.b58decode(b64_bytes))
    with open(f"/home/shahbazi/Desktop/{new_ring_file}","wb") as file:
        file.write(base58.b58decode(b64_bytes))

if __name__ == "__main__":
    get_transaction_value("file13","object4.ring.gz")
    # send_transaction("file13","object.ring.gz")

