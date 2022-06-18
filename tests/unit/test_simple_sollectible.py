from brownie import  network
from scripts.helpful_scripts import get_account , lOCAL_BLOCKCHAIN_ENVO
import pytest 
from scripts.simple_collectible.deploy_and_create import deploy_and_create
def test_can_create_simple_collectible():
    if network.show_active() not in lOCAL_BLOCKCHAIN_ENVO: 
        pytest.skip()
    account = get_account()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == account
    
