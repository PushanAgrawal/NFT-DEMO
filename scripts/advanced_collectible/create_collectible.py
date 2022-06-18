from scripts.helpful_scripts import get_account,fund_with_link
from brownie import AdvancedCollectible

def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    collectible_transaction = advanced_collectible.createCollectible({'from':account})
    collectible_transaction.wait(1)
    print("collectible created")


