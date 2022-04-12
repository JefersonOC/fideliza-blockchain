from web3 import Web3
import json

# I am using Ganache; You can use your Infura link as url
blockchain_address = "HTTP://127.0.0.1:7545"
# Client instance to interact with the blockchain
web3 = Web3(Web3.HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/Token.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xa772c7669A321e411B3Cca0D46F9b40f137aFC05'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']

# Fetch deployed contract reference
contract = web3.eth.contract(
    address=deployed_contract_address, abi=contract_abi)


def get_balance(account):
    try:
        balance = contract.functions.balance(account).call()
        data_set = {
            "address": str(account),
            "balance": str(balance),
        }
        return data_set
    except Exception as e:
        print("Wrong account number: " + str(e))
        return {}


def gift_transfer(account, account_to, amount):
    try:
        tx_hash = contract.functions.transferTokens(
            account_to, int(amount)).transact({'from': account})
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        data_set = {
            "transaction": str(web3.toHex(tx_hash)),
        }
        return data_set
    except Exception as e:
        print("Transaction failed: " + str(e))
        return {}


def gift_redeem(account, amount):
    try:
        tx_hash = contract.functions.redeemTokens(
            int(amount)).transact({'from': account})
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        data_set = {
            "transaction": str(web3.toHex(tx_hash)),
        }
        return data_set
    except Exception as e:
        print("Transaction failed: " + str(e))
        return {}


def poits_mint(account, amount):
    try:
        tx_hash = contract.functions.mint(
            int(amount)).transact({'from': account})
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

        data_set = {
            "transaction": str(web3.toHex(tx_hash)),
        }
        return data_set
    except Exception as e:
        print("Only the owner can mint tokens: " + str(e))
        return {}
