from brownie import accounts, network,  config, Contract, VRFCoordinatorMock, LinkToken, interface
from web3 import Web3

FORKED_LOCAL_ENVO = ['mainnet-fork','mainnet-fork-dev']
lOCAL_BLOCKCHAIN_ENVO=['development','ganache-locals']
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
Decimall=8
starting_price=200000000000
random_to_breed = ['PUG', 'SHIBA_INU', 'ST_BERNARD']

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}



def get_account(index=None, id=None):
    if index:
        return accounts[index]

    if id:
        return  accounts.load(id)     
        

    if network.show_active() in lOCAL_BLOCKCHAIN_ENVO or network.show_active in FORKED_LOCAL_ENVO:
        return accounts[0]

    return  accounts.load("pushanag")      

contract_to_mock = {'vrf_cordinator':VRFCoordinatorMock, 'link_token':LinkToken}    

def get_contract(contract_name):
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in lOCAL_BLOCKCHAIN_ENVO:
        if len(contract_type) <= 0 :
            deploy_mocks()
        contract = contract_type[-1]

    else:
        contract_address = config['networks'][network.show_active()][contract_name]     
        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)

    return contract    

def deploy_mocks():
    print('deploying mock......................')
    
    link_token = LinkToken.deploy({'from':get_account()})
    VRFCoordinatorMock.deploy(link_token.address,{'from':get_account()})
    

    print("mock deployed.....................")  



def fund_with_link(contract_address, account=None, link_token=None, amount=100000000000000000,):
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract('link_token')
    tx = link_token.transfer(contract_address, amount, {'from':account})
    # link_token_contract = interface.LinkTokenInterface(link_token.address)
    # tx= link_token_contract.transfer(contract_address, amount, {'from':account})
    tx.wait(1)
    print('funded')
    return tx


def get_breed(id):
    return random_to_breed[id]
    