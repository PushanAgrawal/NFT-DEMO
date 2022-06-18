from brownie import  network
from scripts.helpful_scripts import get_account, get_contract , lOCAL_BLOCKCHAIN_ENVO
import pytest 
from scripts.advanced_collectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible():

    if network.show_active() not in lOCAL_BLOCKCHAIN_ENVO: 
        pytest.skip()
    account = get_account()
    advanced_collectible, creating_tx = deploy_and_create()
    requestId = creating_tx.events['requestedCollectible']['requestId']
    random_number = 777
    get_contract('vrf_cordinator').callBackWithRandomness(
        requestId,
        random_number,
        advanced_collectible.address,
        {'from':account}
    )
    print (random_number)
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number%3
