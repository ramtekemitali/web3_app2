# build Ethereum dapps(decentralized apps) with python
'''1. write solidity code on Remix IDE 
2. create environment using Ganache - deploy
3. check ganache transaction
4. copy address of deployed Contracts'''

import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org

# Set a default account to sign transactions-this account is unlocked with Ganache
w3.eth.defaultAccount = w3.eth.accounts[0]

# CompilationDetails-web3deploy from solidity Compiler
# Greeter contract ABI
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]');

# Greeter contract address-convert to checksum address
address = w3.toChecksumAddress("0xE764cd4e0C629238691247900584FB590780654b")

# Initialize contract
contract = w3.eth.contract(address=address, abi=abi) 
# Read the default greeting 
# print(contract)
print(contract.functions.greet().call())

# Set a new greeting
tx_hash = contract.functions.setGreeting(' NEW GREETING!').transact()
# print(tx_hash)
'''for upgraded greeting'''

# Wait for the transaction to be mined
w3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated greeting: {}'.format(
    contract.functions.greet().call()
))
