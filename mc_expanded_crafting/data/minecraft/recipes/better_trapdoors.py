import json
import os

if __name__ == '__main__':
    dir = os.getcwd()
    wood_types = ['oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'warped', 'crimson']

    # Deletes all alternate_{type}_trapdoor.json files in the current
    # directory. Should only be used when developing/testing. Otherwise, should
    # be disabled.
    # for file in os.listdir(dir):
    #     if 'trapdoor' in file and '.json' in file:
    #         os.remove(file)

    for type in wood_types:
        output_file_name = 'alternate_{}_trapdoor.json'.format(type)
        contents = json.dumps({
            "type": "minecraft:crafting_shaped",
            "pattern": [
                "###",
                "###"
            ],
            "key": {
                "#": {
                    "item": "minecraft:{}_planks".format(type)
                }
            },
            "result": {
                "item": "minecraft:{}_trapdoor".format(type),
                "count": 12
            }
        })
            
        file = '{}/{}'.format(dir, output_file_name)
        with open(file, 'w') as file:
            file.write(contents)

    output_file_name = 'alternate_iron_trapdoor.json'.format(type)
    contents = json.dumps({
        "type": "minecraft:crafting_shaped",
        "pattern": [
            "###",
            "###"
        ],
        "key": {
            "#": {
                "item": "minecraft:iron_ingot".format(type)
            }
        },
        "result": {
            "item": "minecraft:iron_trapdoor".format(type),
            "count": 12
        }
    })
        
    file = '{}/{}'.format(dir, output_file_name)
    with open(file, 'w') as file:
        file.write(contents)