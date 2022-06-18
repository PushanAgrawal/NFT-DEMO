from brownie import  network
from scripts.helpful_scripts import get_account, get_contract , lOCAL_BLOCKCHAIN_ENVO
import pytest 
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time

def test_can_create_advanced_collectible_integration():

    if network.show_active()  in lOCAL_BLOCKCHAIN_ENVO: 
        pytest.skip()
    account = get_account()
    advanced_collectible, creating_tx = deploy_and_create()
    time.sleep(60)

    
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number%3
