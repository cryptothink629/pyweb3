
from web3 import Web3
from web3.middleware import geth_poa_middleware
import os

w3 = Web3(Web3.HTTPProvider(os.environ.get('GETH_HOST')))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print('web3 connection: ' + str(w3.isConnected()))

ac1 = w3.eth.accounts[0]
ac2 = w3.eth.accounts[1]

tx_hash = w3.eth.send_transaction({
   'from': ac1,
   'to': ac2,
   'value': w3.toWei(0.001, 'ether')
})
w3.eth.wait_for_transaction_receipt(tx_hash)

tx = w3.eth.get_transaction(tx_hash)
print(tx)



