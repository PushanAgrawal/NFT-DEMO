from brownie import AdvancedCollectible, accounts, network
from scripts.helpful_scripts import get_account, get_breed


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectible = advanced_collectible.tokenCounter()

    for token_id in range(number_of_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            set_tokenuri(advanced_collectible, token_id, tokenUri)

def set_tokenuri(nft_contract, token_id, tokenUri):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenUri, {"from":account})
    tx.wait(1)
    
    
