import os
import json
import requests
from scripts.helpful_scripts import get_account,fund_with_link, get_breed , breed_to_image_uri
from brownie import AdvancedCollectible , network
from metadata.sample_metadata import metadata_template
from pathlib import Path



def main():
    # account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectible = advanced_collectible.tokenCounter()
    
    
    for token_id in range(number_of_advanced_collectible) :
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print("the  metadata already exists")
        else:
            print("creating metadata file")    
            collectible_metadata['name'] = breed
            collectible_metadata['description'] = f"An adorable {breed} pup!"
            image_path = "./img/" + breed.lower().replace('_','-') + '.png'
            if  os.getenv('UPLOAD_IPFS') == 'true':
                image_url = upload_to_ipfs(image_path)
            image_url = image_url if image_url else breed_to_image_uri[breed]    
            collectible_metadata['image'] = image_url
            with open(metadata_file_name, 'w') as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)
            print(collectible_metadata, ipfs_uriii)
            

def upload_to_ipfs(file_path):
    with Path(file_path).open('rb') as fp:
        image_binary = fp.read()
        ipfs_url = 'http://127.0.0.1:5001'
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files ={'file':image_binary})
        img_hash = response.json()['Hash']
        file_name = file_path.split('/')[-1:][0]
        img_uri = f"https://ipfs.io/ipfs/{img_hash}?filename={file_name}"
        print(img_uri)
        return img_uri
                