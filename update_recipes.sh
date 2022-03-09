DIR="$( cd "$( dirname "$0" )" && pwd )"
REPO="https://github.com/Michaelcraun/MCCrafting.git"
TEMP="$DIR/tmp"

# Clone the repo fresh
git clone "$REPO" "$TEMP"

# Sync the tmp folder with the datapacks folder
echo "Syncing datapacks..."
rsync -a "$TEMP/" "$DIR/"

# Clean up
echo "Cleaning up..."
rm "$DIR/newpack.sh"
rm "$DIR/README.md"
rm -rf "$DIR/src"
rm "$DIR/unpack.sh"
rm -rf "$TEMP"