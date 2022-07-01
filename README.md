# This is a eth dev demo project

create file `.env` add your `WEB3_INFURA_PROJECT_ID` and `ETHERSCAN_TOKEN` to it.



### active venv
```
source ./venv/bin/activate
```

### compile contracts
```
brownie compile
```

### deploy on ropsten network
```
brownie run ./scripts/deploy_NFT.py --network 'ropsten'
```
