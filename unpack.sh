for file in *
do
    if [ $file == "unpack.sh" ] 
    then
        echo "Skipping unpack.sh..."
    elif [ $file == "newpack.sh" ] 
    then
        echo "Skipping newpack.sh..."
    elif [ $file == "README.md" ]
    then 
        echo "Skipping README.md..."
    elif [ $file == "src" ]
    then
        echo "Skipping src directory..."
    else
        cp -r $file ..
    fi
done