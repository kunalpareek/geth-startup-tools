## Installation using binary

`wget https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.8.15-89451f7c.tar.gz`

`tar -xzf geth-linux-amd64-1.8.15-89451f7c.tar.gz`

`cp geth-linux-amd64-1.8.15-89451f7c/geth .`

`rm -rf geth-linux-amd64-1.8.15-89451f7c`

`mkdir data`

## Installation using ppa

`sudo add-apt-repository -y ppa:ethereum/ethereum`

`sudo apt-get update`

`sudo apt-get install ethereum`

`mkdir data`

## Initialize bootnode

`bootnode -genkey boot.key`

## Start bootnode

`bootnode -nodekey boot.key`

Copy the enode address that appears on the console.

Note : Run bootnode in a screen using screen commands.

## Create new account

`geth --datadir data/ account new`

## Create genesis

Note : Create genesis only once for a network. Copy the genesis to all the instances that are going to run on the network.

`python genesis.py --chain_id "[chain id]" --prefunded_accounts "182d8bd276cca922c26f3f84a0a5d725cddbb3a3" --sealer_accounts "182d8bd276cca922c26f3f84a0a5d725cddbb3a3"`

The above step creates a genesis.json file which will be used to initialize all the nodes in the network.

## Initialize the node

`geth --datadir data/ init genesis.json`

## Run node as a sealer

1. Run geth as a background process

`nohup geth --datadir data/ --bootnodes 'enode address of bootnode' &`

2. Open geth javascript console

`geth attach data/geth.ipc`

3. Unlock sealer account

`personal.unlockAcoount("sealerAccountAddress", "sealerAccountPassword", 0)`

4. Start miner

`miner.start()`

5. Exit console
`CTRL + d`

## Run node with rpc api's opened

`nohup geth --datadir data/ --bootnodes 'enode address of bootnode' --rpc --ws --rpccorsdomain '*' --wsorigins '*' &`

Note : On production change rpccorsdomain and wsorigins to your domain.
