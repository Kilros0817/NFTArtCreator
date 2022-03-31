import json
import os

root = "data/pot"
NEW_JSON_DIR = "newjson"

def convert_data(rarity):
    total_cnt = len(os.listdir(f"{root}/{rarity}/json"))
    if os.path.isdir(f"{root}/{rarity}/newJson") == False:
        os.mkdir(f"{root}/{rarity}/newJson")
    for i in range(0, total_cnt):
        print(f"processing {i}th file...")
        json_path = f"{root}/{rarity}/json/{i + 1}.json"
        f = open(json_path, "r")
        json_str = f.read()
        f.close()
        json_data = json.loads(json_str)

        new_json_data = {
            "name": f"CDSNFT-Pot-{rarity} #{i + 1}",
            "description": f"{rarity} Pot Token #{i + 1}",
            "external_url": "",
            "image": f"replace/{i + 1}.jpg",
            "price": f"{rarity}",
            "attributes": [
                {
                    "trait_type": "background",
                    "value": str(json_data["background"]["imageName"])
                }, {
                    "trait_type": "backeffect",
                    "value": str(json_data["backeffect"]["imageName"])
                }, {
                    "trait_type": "layer2",
                    "value": str(json_data["layer2"]["imageName"])
                }, {
                    "trait_type": "layer1",
                    "value": str(json_data["layer1"]["imageName"])
                }, {
                    "trait_type": "layer0",
                    "value": str(json_data["layer0"]["imageName"])
                }, {
                    "trait_type": "plant",
                    "value": str(json_data["plant"]["imageName"])
                }, {
                    "trait_type": "chill",
                    "value": str(json_data["chill"]["imageName"])
                }, {
                    "trait_type": "border",
                    "value": str(json_data["border"]["imageName"])
                }
            ],
            
        }
        json_str = json.dumps(new_json_data, indent=2)
        json_path = f"{root}/{rarity}/newJson/{i + 1}"
        f = open(json_path, "w")
        f.write(json_str)
        f.close()

    print("finished generating all JSONS.")


if __name__ == '__main__':
    convert_data("Diamond")
    convert_data("Ruby")
    convert_data("Pearl")
    convert_data("Carbon")
