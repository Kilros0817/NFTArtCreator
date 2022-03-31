from PIL import Image
import random
import json
import os

####for creating pot images
from modelP import background_data
from modelP import background_effect_data
from modelP import layer_2_data
from modelP import layer_1_data
from modelP import layer_0_data
from modelP import plant_data
from modelP import chill_data
from modelP import border_data

#total nft count : have to change for each type of token. 
#field: 1000, yard: 10000, pot: 100000
TOTAL_NFT_COUNT = 100000

DATA_DIR = "data"
JSON_DIR = "json"
IMAGE_DIR = "images"

#####path for source traits. change to field, yard, pot respectly
pot_img_path = "assets/pot"

pot_diamond_path = "data/pot/diamond"
pot_ruby_path = "data/pot/ruby"
pot_pearl_path = "data/pot/pearl"
pot_carbon_path = "data/pot/carbon"

os.mkdir(pot_diamond_path)
os.mkdir(f"{pot_diamond_path}/image")
os.mkdir(f"{pot_diamond_path}/json")
os.mkdir(pot_ruby_path)
os.mkdir(f"{pot_ruby_path}/image")
os.mkdir(f"{pot_ruby_path}/json")
os.mkdir(pot_pearl_path)
os.mkdir(f"{pot_pearl_path}/image")
os.mkdir(f"{pot_pearl_path}/json")
os.mkdir(pot_carbon_path)
os.mkdir(f"{pot_carbon_path}/image")
os.mkdir(f"{pot_carbon_path}/json")


def choose_by_rarity(data):
    return random.choices(data, [item['chance'] for item in data])

def generate_pot_nfts():
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
        chill = choose_by_rarity(chill_data)[0]
        border = choose_by_rarity(border_data)[0]
        
        if diamond == 200 and border["rarity"] == "Diamond":
            i -= 1
            continue
        if ruby == 1000 and border["rarity"] == "Ruby":
            i -= 1
            continue
        if pearl == 49400 and border["rarity"] == "Pearl":
            i -= 1
            continue
        if carbon == 49400 and border["rarity"] == "Carbon":
            i -= 1
            continue
        
        print(f"generating {i}th NFT...")
        
        image = generate_pot_nft(background, backeffect, layer2, layer1, layer0, plant,
                                  chill, border)
        
        json_data = {
            "background": { "imageName": background["imageName"], "rarity": background["rarity"] },
            "backeffect": { "imageName": backeffect["imageName"], "rarity": backeffect["rarity"] },
            "layer2": { "imageName": layer2["imageName"], "rarity": layer2["rarity"] },
            "layer1": { "imageName": layer1["imageName"], "rarity": layer1["rarity"] },
            "layer0": { "imageName": layer0["imageName"], "rarity": layer0["rarity"] },
            "plant": { "imageName": plant["imageName"], "rarity": plant["rarity"] },
            "chill": { "imageName": chill["imageName"], "rarity": chill["rarity"] },
            "border": { "imageName": border["imageName"], "rarity": border["rarity"] },
        }
        
        image_path = ""
        json_path = ""
        if border["rarity"] == "Diamond":
            diamond += 1
            image_path = f"{pot_diamond_path}/image/{diamond}.jpg"
            json_path = f"{pot_diamond_path}/json/{diamond}.json"
            
        if border["rarity"] == "Ruby":
            ruby += 1
            image_path = f"{pot_ruby_path}/image/{ruby}.jpg"
            json_path = f"{pot_ruby_path}/json/{ruby}.json"
            
        if border["rarity"] == "Pearl":
            pearl += 1
            image_path = f"{pot_pearl_path}/image/{pearl}.jpg"
            json_path = f"{pot_pearl_path}/json/{pearl}.json"
        
        if border["rarity"] == "Carbon":
            carbon += 1
            image_path = f"{pot_carbon_path}/image/{carbon}.jpg"
            json_path = f"{pot_carbon_path}/json/{carbon}.json"
        # save image
        image = image.convert('RGB')
        image.save(image_path)
        # save json
        json_str = json.dumps(json_data, indent=2)
        f = open(json_path, "w")
        f.write(json_str)
        f.close()
        
    print("finished generating all pot NFTs.")


def generate_pot_nft(background, backeffect, layer2, layer1, layer0, plant, 
          chill, border):
    background = Image.open(f"{pot_img_path}/0 - BACKGROUND/{background['imageName']}.png").convert("RGBA")
    backeffect = Image.open(f"{pot_img_path}/1 - BACKGROUND EFFECTS/{backeffect['imageName']}.png").convert("RGBA")
    layer2 = Image.open(f"{pot_img_path}/2 - LAND LAYERS(2)/{layer2['imageName']}.png").convert("RGBA")
    layer1 = Image.open(f"{pot_img_path}/3 - LAND LAYERS(1)/{layer1['imageName']}.png").convert("RGBA")
    layer0 = Image.open(f"{pot_img_path}/4 - LAND LAYERS(0)/{layer0['imageName']}.png").convert("RGBA")
    plant = Image.open(f"{pot_img_path}/5 - BUILDINGS, PLANTS _ ANIMALS/{plant['imageName']}.png").convert("RGBA")
    chill = Image.open(f"{pot_img_path}/6 - CHILL, VEHICLES _ SPECIALS/{chill['imageName']}.png").convert("RGBA")
    border = Image.open(f"{pot_img_path}/7 - BORDERS REWARDS/{border['imageName']}.png").convert("RGBA")
    background.paste(backeffect, (0, 0), backeffect)
    background.paste(layer2, (0, 0), layer2)
    background.paste(layer1, (0, 0), layer1)
    background.paste(layer0, (0, 0), layer0)
    background.paste(plant, (0, 0), plant)
    background.paste(chill, (0, 0), chill)
    background.paste(border, (0, 0), border)
    return background

if __name__ == '__main__':
    generate_pot_nfts()