from web3 import Web3

infura_mainnet_url = 'https://mainnet.infura.io/v3/c66311e1efb04a0b8bb0e1b2177b54cc'
infura_ropsten_url = 'https://ropsten.infura.io/v3/c66311e1efb04a0b8bb0e1b2177b54cc'

web3 = Web3(Web3.HTTPProvider(infura_ropsten_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

account = '0x***'

balance = web3.eth.getBalance(account)
print(web3.fromWei(balance, "ether"))

