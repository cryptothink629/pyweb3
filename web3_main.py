import os

from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider(os.environ.get('GETH_HOST')))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print('web3 connection: ' + str(w3.isConnected()))


def transfer(from_, to_, value):
    tx_hash = w3.eth.send_transaction({
        'from': from_,
        'to': to_,
        'value': value
    })
    w3.eth.wait_for_transaction_receipt(tx_hash)

    tx = w3.eth.get_transaction(tx_hash)
    print(tx)
    return tx


def create_number_contract(abi, bytecode):
    n = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = n.constructor(1).transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(tx_receipt)
    return tx_receipt


def call_number(abi, address):
    g = w3.eth.contract(address=address, abi=abi)
    g.functions.get().call()


def set_number(abi, address):
    g = w3.eth.contract(address=address, abi=abi)
    tx_hash = g.functions.set(1).transact()
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    g.functions.greet().call()


def main():
    ac1 = w3.eth.accounts[0]
    ac2 = w3.eth.accounts[1]

    w3.eth.default_account = w3.eth.accounts[0]
    value = w3.toWei(0.001, 'ether')

    transfer(ac1, ac2, value)

    from brownie import Number
    abi = Number.abi
    bytecode = Number.bytecode
    tx_receipt = create_number_contract(abi, bytecode)
    address = tx_receipt.address  # '0x901a6151076Af632A413e8a8D1ADEC1f8Dc80859'

    call_number(abi, address)

    set_number(abi, address)


if __name__ == '__main__':
    main()
