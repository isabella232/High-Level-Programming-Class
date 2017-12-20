# echo "$(($num1+$num2))"

# find sum
if [ "$1" == "S" ]; then
    for i in ${@:2}; do
        declare -i i
        sum=$(expr $sum + $i)
    done
    echo $sum
fi

# find product
if [ "$1" == "P" ]; then
    prod=1
    declare -i prod
    for i in ${@:2}; do
        let "prod*=i"
    done
    echo $prod
fi

# find maximum
if [ "$1" == "M" ]; then
    let "max=$2"
    for i in ${@:3}; do
        if [ "$i" -gt "$max" ]; then
            let "max=i"
        fi
    done
    echo $max
fi

# find minimum
if [ "$1" == "m" ]; then
    let "min=$2"
    for i in ${@:3}; do
        if [ "$i" -lt "$min" ]; then
            let "min=i"
        fi
    done
    echo $min
fi
