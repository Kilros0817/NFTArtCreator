from PIL import Image
import random
import json
import os

###for creating yard images
from modelY import background_data
from modelY import background_effect_data
from modelY import layer_2_data
from modelY import layer_1_data
from modelY import layer_0_data
from modelY import plant_data
from modelY import building_data
from modelY import chill_data
from modelY import special_data
from modelY import border_data

#total nft count : have to change for each type of token. 
#field: 1000, yard: 10000, pot: 100000
TOTAL_NFT_COUNT = 10000

DATA_DIR = "data"
JSON_DIR = "json"
IMAGE_DIR = "images"

#####path for source traits. change to field, yard, pot respectly
yard_img_path = "assets/yard"

yard_diamond_path = "data/yard/diamond"
yard_ruby_path = "data/yard/ruby"
yard_pearl_path = "data/yard/pearl"
yard_carbon_path = "data/yard/carbon"

os.mkdir(yard_diamond_path)
os.mkdir(f"{yard_diamond_path}/image")
os.mkdir(f"{yard_diamond_path}/json")
os.mkdir(yard_ruby_path)
os.mkdir(f"{yard_ruby_path}/image")
os.mkdir(f"{yard_ruby_path}/json")
os.mkdir(yard_pearl_path)
os.mkdir(f"{yard_pearl_path}/image")
os.mkdir(f"{yard_pearl_path}/json")
os.mkdir(yard_carbon_path)
os.mkdir(f"{yard_carbon_path}/image")
os.mkdir(f"{yard_carbon_path}/json")


def choose_by_rarity(data):
    return random.choices(data, [item['chance'] for item in data])

    
def generate_yard_nfts():
    diamond = 0
    ruby = 0
    pearl = 0
    carbon = 0
    i = 0
    while i < TOTAL_NFT_COUNT:
        i += 1
        
        background = choose_by_rarity(background_data)[0]
        backeffect = choose_by_rarity(background_effect_data)[0]
        layer2 = choose_by_rarity(layer_2_data)[0]
        layer1 = choose_by_rarity(layer_1_data)[0]
        layer0 = choose_by_rarity(layer_0_data)[0]
        plant = choose_by_rarity(plant_data)[0]
        building = choose_by_rarity(building_data)[0]
        chill = choose_by_rarity(chill_data)[0]
        special = choose_by_rarity(special_data)[0]
        border = choose_by_rarity(border_data)[0]
        
        if diamond == 20 and border["rarity"] == "Diamond":
            i -= 1
            continue
        if ruby == 100 and border["rarity"] == "Ruby":
            i -= 1
            continue
        if pearl == 4940 and border["rarity"] == "Pearl":
            i -= 1
            continue
        if carbon == 4940 and border["rarity"] == "Carbon":
            i -= 1
            continue
        
        image = generate_yard_nft(background, backeffect, layer2, layer1, layer0, plant, 
                              building, chill, special, border)
        print(f"generating {i}th NFT...")
        json_data = {
            "background": { "imageName": background["imageName"], "rarity": background["rarity"] },
            "backeffect": { "imageName": backeffect["imageName"], "rarity": backeffect["rarity"] },
            "layer2": { "imageName": layer2["imageName"], "rarity": layer2["rarity"] },
            "layer1": { "imageName": layer1["imageName"], "rarity": layer1["rarity"] },
            "layer0": { "imageName": layer0["imageName"], "rarity": layer0["rarity"] },
            "plant": { "imageName": plant["imageName"], "rarity": plant["rarity"] },
            "building": { "imageName": building["imageName"], "rarity": building["rarity"] },
            "chill": { "imageName": chill["imageName"], "rarity": chill["rarity"] },
            "special": { "imageName": special["imageName"], "rarity": special["rarity"] },
            "border": { "imageName": border["imageName"], "rarity": border["rarity"] },
        }
        # save image
        
        image_path = ""
        json_path = ""
        if border["rarity"] == "Diamond":
            diamond += 1
            image_path = f"{yard_diamond_path}/image/{diamond}.jpg"
            json_path = f"{yard_diamond_path}/json/{diamond}.json"
            
        if border["rarity"] == "Ruby":
            ruby += 1
            image_path = f"{yard_ruby_path}/image/{ruby}.jpg"
            json_path = f"{yard_ruby_path}/json/{ruby}.json"
            
        if border["rarity"] == "Pearl":
            pearl += 1
            image_path = f"{yard_pearl_path}/image/{pearl}.jpg"
            json_path = f"{yard_pearl_path}/json/{pearl}.json"
        
        if border["rarity"] == "Carbon":
            carbon += 1
            image_path = f"{yard_carbon_path}/image/{carbon}.jpg"
            json_path = f"{yard_carbon_path}/json/{carbon}.json"
            
        image = image.convert('RGB')
        image.save(image_path)
        # save json
        json_str = json.dumps(json_data, indent=2)
        f = open(json_path, "w")
        f.write(json_str)
        f.close()
        
    print("finished generating all yard NFTs.")
    

def generate_yard_nft(background, backeffect, layer2, layer1, layer0, plant, 
              building, chill, special, border):
    background = Image.open(f"{yard_img_path}/0 - BACKGROUND/{background['imageName']}.png").convert("RGBA")
    backeffect = Image.open(f"{yard_img_path}/1 - BACKGROUND EFFECTS/{backeffect['imageName']}.png").convert("RGBA")
    layer2 = Image.open(f"{yard_img_path}/2 - LAND LAYERS(2)/{layer2['imageName']}.png").convert("RGBA")
    layer1 = Image.open(f"{yard_img_path}/3 - LAND LAYERS(1)/{layer1['imageName']}.png").convert("RGBA")
    layer0 = Image.open(f"{yard_img_path}/4 - LAND LAYERS(0)/{layer0['imageName']}.png").convert("RGBA")
    building = Image.open(f"{yard_img_path}/5 - BUILDINGS/{building['imageName']}.png").convert("RGBA")
    plant = Image.open(f"{yard_img_path}/6 - PLANTS _ ANIMALS/{plant['imageName']}.png").convert("RGBA")
    chill = Image.open(f"{yard_img_path}/7 - CHILL _ VEHICLES/{chill['imageName']}.png").convert("RGBA")
    special = Image.open(f"{yard_img_path}/8 - SPECIALS/{special['imageName']}.png").convert("RGBA")
    border = Image.open(f"{yard_img_path}/9 - BORDERS REWARDS/{border['imageName']}.png").convert("RGBA")
    background.paste(backeffect, (0, 0), backeffect)
    background.paste(layer2, (0, 0), layer2)
    background.paste(layer1, (0, 0), layer1)
    background.paste(layer0, (0, 0), layer0)
    background.paste(plant, (0, 0), plant)
    background.paste(building, (0, 0), building)
    background.paste(chill, (0, 0), chill)
    background.paste(special, (0, 0), special)
    background.paste(border, (0, 0), border)
    
    return background

if __name__ == '__main__':
    generate_yard_nfts()
