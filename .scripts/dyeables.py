'''
A small module created for easily creating Minecraft crafting recipes for
applying dyes to dyable blocks. The intention is that you should be able to
apply dye to already dyed items and get a new item in the color you want.
'''

import json
import os

root_dir = os.path.dirname(__file__)
data_dir = os.path.join(root_dir, 'data')
recipe_dir = os.path.join(data_dir, 'minecraft/recipes')

colors = [
    'black',
    'blue',
    'brown',
    'cyan',
    'gray',
    'green',
    'light_blue',
    'light_gray',
    'lime',
    'magenta',
    'orange',
    'pink',
    'purple',
    'red',
    'white',
    'yellow'
]
dyeable_items = [
    'candle',
    'carpet',
    'concrete_powder',
    'glass',
    'stained_glass_pane',
    'terracotta',
    'wool'
]

def create_tag(item_type: str) -> dict:
    '''Creates an item tag for a set of Minecraft items for later use.'''
    values = map(lambda color: f"minecraft:{color}_{item_type}", colors)
    return {
        "replace" : False,
        "values" : list(values)
    }

def create_recipe(tag: str, item_type: str, color: str) -> dict:
    '''Creates the recipe object for later parsing.'''
    return {
        "type" : "minecraft:crafting_shaped",
        "pattern" : [
            "###",
            "#R#",
            "###"
        ],
        "key" : {
            "#" : {
                "tag" : f"{tag}:any_{item_type}"
            },
            "R": {
                "item" : f"minecraft:{color}_dye"
            }
        },
        "result" : {
            "item" : f"minecraft:{color}_{item_type}",
            "count" : 8
        }
    }

def get_tag_identifier() -> str:
    '''Fetches the name of the item group based off of the directory setup.'''
    for directory in os.listdir(data_dir):
        path = os.path.join(data_dir, directory)
        if os.path.isdir(path) and directory != 'minecraft':
            return directory
    raise IOError('Tag directory does not exist!')

if __name__ == '__main__':
    tag_identifier = get_tag_identifier()
    tag_dir = os.path.join(data_dir, f'{tag_identifier}/tags/items')

    for item in dyeable_items:
        # Create tag file
        item_tag = create_tag(item)
        tag_path = os.path.join(tag_dir, f'any_{item}.json')

        with open(tag_path, 'w') as file:
            tag_json = json.dumps(item_tag)
            file.write(tag_json)

        for color_name in colors:
            file_name = f'dyeable_{color_name}_{item}.json'
            recipe_path = os.path.join(recipe_dir, file_name)
            recipe = create_recipe(tag_identifier, item, color_name)

            with open(recipe_path, 'w') as file:
                recipe_json = json.dumps(recipe)
                file.write(recipe_json)
