from web3 import Web3

infura_mainnet_url = 'https://mainnet.infura.io/v3/***'
infura_ropsten_url = 'https://ropsten.infura.io/v3/***'

web3 = Web3(Web3.HTTPProvider(infura_ropsten_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

account = '0x***'

balance = web3.eth.getBalance(account)
print(web3.fromWei(balance, "ether"))

