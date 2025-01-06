from web3 import Web3, AsyncWeb3

print("*Start")
w3 = Web3(Web3.HTTPProvider('http://137.131.180.21:8545'))
if w3.is_connected():
    print("Connected to blockchain")
    balance = w3.eth.get_balance('0x8f401f28a4993894EFA3f39f962c34D33e16F9cB')
    print(f"balance = {balance}")
else:
    print("Error connecting to blockchain")
print("*End")