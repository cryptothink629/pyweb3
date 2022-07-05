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

### brownie add network
```
brownie networks add Ethereum mainnet-geth host=/root/.ethereum/geth.ipc name=Mainnet-Geth chainid=1
brownie networks add Ethereum goerli-geth host=/root/.ethereum/goerli/geth.ipc name=Goerli-Geth chainid=5
```

### Geth run light client
```
nohup geth --syncmode light --http --http.addr 0.0.0.0   > out 2>&1 &
nohup geth --syncmode light --http --http.addr 0.0.0.0  --goerli > out 2>&1 &
nohup geth --syncmode light --http --http.addr 0.0.0.0  --goerli --unlock <account> --password <password file>  --allow-insecure-unlock > out 2>&1 &

```