#!/bin/bash

packname=$1
namespace=$2

mkdir "$packname"
mkdir "$packname/data"
mkdir "$packname/data/minecraft"
mkdir "$packname/data/minecraft/recipes"
mkdir "$packname/data/$namespace"
mkdir "$packname/data/$namespace/tags"
mkdir "$packname/data/$namespace/tags/items"

packmeta="""{
     \"pack\" : { 
         \"pack_format\" : 1, 
         \"description\" : \"$namespace\" 
     } 
}"""
echo "$packmeta" >> "$packname/pack.mcmeta"

echo "Please add recipes to the $packname/data/minecraft/recipes directory"
echo "Please add any tags to the $packname/data/$namespace/tags/items directory"