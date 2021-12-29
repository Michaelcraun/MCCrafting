DIR="$( cd "$( dirname "$0" )" && pwd )"
REPO="https://github.com/Michaelcraun/MCCrafting.git"
TEMP="$DIR/tmp"
DATAPACKS="$DIR/datapacks"

# Clone the repo fresh
git clone $REPO tmp

# Sync the tmp folder with the datapacks folder
rsync -a -v "$TEMP/" "$DATAPACKS/"

# Clean up
rm "$DATAPACKS/newpack.sh"
rm "$DATAPACKS/README.md"
rm -rf "$DATAPACKS/src"
rm "$DATAPACKS/unpack.sh"
rm "$DATAPACKS/update.sh"
mv "$DATAPACKS/update_recipes.sh" "$DATAPACKS/../update_recipes.sh"
rm -rf "$TEMP"