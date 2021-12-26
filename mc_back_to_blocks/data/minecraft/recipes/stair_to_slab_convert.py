import json
import os

if __name__ == '__main__':
    dir = os.getcwd()

    # Deletes all {base_item_name}s_to_{blocks/planks}.json files in the current
    # directory. Should only be used when developing/testing. Otherwise, should
    # be disabled.
    # for file in os.listdir(dir):
    #     if 'slab' in file and '.json' in file:
    #         os.remove(file)

    for file in os.listdir(dir):
        if '.DS_Store' not in file:
            base_item_name = file.replace('_stairs_to_planks.json', '')
            base_item_name = base_item_name.replace('_stairs_to_blocks.json', '')
            input_item_name = '{}_slab'.format(base_item_name)
            output_item_name = base_item_name
            output_file_name = ''

            if 'planks' in file:
                output_item_name = '{}_planks'.format(base_item_name)
                output_file_name = '{}s_to_planks.json'.format(input_item_name)
            else:
                output_file_name = '{}s_to_blocks.json'.format(input_item_name)

            # 3 blocks = 6 slabs
            # 6 slabs = 3 blocks
            contents = json.dumps({
                "type" : "minecraft:crafting_shapeless",
                "ingredients" : [
                    {
                        "item" : "minecraft:{}".format(input_item_name)
                    },
                    {
                        "item" : "minecraft:{}".format(input_item_name)
                    },
                    {
                        "item" : "minecraft:{}".format(input_item_name)
                    },
                    {
                        "item" : "minecraft:{}".format(input_item_name)
                    },
                    {
                        "item" : "minecraft:{}".format(input_item_name)
                    },
                    {
                        "item" : "minecraft:{}".format(input_item_name)
                    }
                ],
                "result" : {
                    "item" : "minecraft:{}".format(output_item_name),
                    "count" : 3
                }
            })
            
            file = '{}/{}'.format(dir, output_file_name)
            with open(file, 'w') as file:
                file.write(contents)