
# change to ropsten network
from brownie import network
network.disconnect()
network.connect('ropsten')
network.connect('mainnet')
network.show_active()

from brownie import Contract, accounts

c = Contract('0x5caf109Ec2801c3b3e5fcD814fB1C2371F2A66d8')
c.abi
c.alias
acct = accounts.load('1')  # load external account
c.setA(101, {'from': acct})
c.sendViaCall('0x3f39Bc16ef847C0Cc74b751C4316109B7977c872', {'from': acct, 'value': '0.001 ether'} )
c.withdraw('0.05 ether', {'from': acct})

# send ether from account to contract
acct = accounts.load('1')  # load external account
acct.transfer('0x5caf109Ec2801c3b3e5fcD814fB1C2371F2A66d8', '0.01 ether')

# mint
c = Contract.from_explorer('0xC5b68b46308927242e8a6E0AA0bE44cBF3C3e322') # first time import
c.mint(1, {'from': acct, 'value': '0.002 ether'})

# interact with web3 (do not connect dev net)
# chain
# web3.eth.block_number


