import time
import json
import argparse

class Genesis:
    """
    Genesis config for Ethereum Proof of Authority blockchain
    """
    def __init__(self, chain_id):
        """
        Genesis constructor
        :param chain_id: int unique chain / network identifier
        """
        self.config = {
            "chainId": chain_id,
            "homesteadBlock": 1,
            "eip150Block": 2,
            "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
            "eip155Block": 3,
            "eip158Block": 3,
            "byzantiumBlock": 4,
            "clique": {
            "period": 5,
            "epoch": 30000
            }
        }
        self.nonce = "0x0"
        self.timestamp = hex(int(time.time()))
        self.extra_data = ""
        self.gas_limit = "0xBEBC200"
        self.difficulty = "0x1"
        self.mix_hash = "0x0000000000000000000000000000000000000000000000000000000000000000"
        self.coinbase = "0x0000000000000000000000000000000000000000"
        self.number = "0x0"
        self.gas_used = "0x0"
        self.parent_hash = "0x0000000000000000000000000000000000000000000000000000000000000000"
        self.alloc = dict({"0x0000000000000000000000000000000000000000":"0x1"})
    
    def add_prefunded_accounts(self, prefunded_accounts):
        """
        :param prefunded_accounts: (string comma separated) accounts to be prefunded
        """
        temp = {}
        for account in prefunded_accounts.split(","):
            if account[0:2] <> "0x" and len(account) == 40:
                temp[account] = {}
                temp[account]["balance"] = "0x200000000000000000000000000000000000000000000000000000000000000"
            elif account[0:2] == "0x" and len(account) == 42:
                temp[account] = {}
                temp[account]["balance"] = "0x200000000000000000000000000000000000000000000000000000000000000"
            else:
                print "account format not recognized"
        self.alloc = temp
    
    def add_sealer_accounts(self, sealer_accounts):
        """
        :param sealer_accounts: (string comma separated) accounts to be sealers
        """
        self.extra_data = "0x0000000000000000000000000000000000000000000000000000000000000000"
        for account in sealer_accounts.split(","):
            if account[0:2] <> "0x" and len(account) == 40:
                self.extra_data += account
            elif account[0:2] == "0x" and len(account) == 42:
                self.extra_data += account[2:]
            else:
                print "account format not recognized"
        self.extra_data += "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    

    def dump_genesis(self, filename):
        """
        :param filename: string
        """
        genesis = {
            "config": self.config,
            "nonce": self.nonce,
            "timestamp": self.timestamp,
            "extraData": self.extra_data,
            "gasLimit": self.gas_limit,
            "difficulty": self.difficulty,
            "mixHash": self.mix_hash,
            "coinbase": self.coinbase,
            "alloc": self.alloc,
            "number": self.number,
            "gasUsed": self.gas_used,
            "parentHash": self.parent_hash
        }
        f = open(filename, 'w')
        f.write(json.dumps(genesis, indent = 4))
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--chain_id', help='chain id or network unique identifier')
    parser.add_argument('--prefunded_accounts', help='comma separated list of accounts to be prefunded')
    parser.add_argument('--sealer_accounts', help='comma separated list of accounts to be sealers')
    parser.add_argument('--filename', help='file to store genesis config')

    args = parser.parse_args()

    if not args.filename:
        args.filename = "genesis.json"

    if args.chain_id and args.prefunded_accounts and args.sealer_accounts:
        try:
            genesis = Genesis(int(args.chain_id))
            genesis.add_sealer_accounts(args.sealer_accounts)
            genesis.add_prefunded_accounts(args.prefunded_accounts)
            genesis.dump_genesis(args.filename)
        except ValueError:
            print "invalid chain id. use only numbers"
        except Exception as e:
            print e
    else:
        print "please provide sufficient arguments"


