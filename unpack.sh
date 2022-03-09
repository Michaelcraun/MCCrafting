DIR=$1

if [ "$DIR" == "" ]; then
    echo "An installation directory is required, please try again!"
    exit
fi

echo "Unpacking custom recipes..."

for file in *
do
    if [ $file == "unpack.sh" ]; then
        echo "Skipping unpack.sh..."
    elif [ $file == "newpack.sh" ]; then
        echo "Skipping newpack.sh..."
    elif [ $file == "README.md" ]; then 
        echo "Skipping README.md..."
    elif [ $file == "src" ]; then
        echo "Skipping src directory..."
    elif [ $file == "update.sh" ]; then 
        cp -r "$file" "$DIR"
    elif [ $file == "update_recipes.sh" ]; then
        cp -r "$file" "$DIR"
    else
        cp -r "$file" "$DIR"
    fi
done

rm -rf "$( cd "$( dirname "$0" )" && pwd )"