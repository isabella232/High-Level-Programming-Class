while true;
do
    clear && printf '\e[3J'
    if [ $# > 0 ]; then
        if [ "$1" == "us" ]; then
                TZ='America/New_York' date +"%T"
        fi
    fi
    if [ $# -ne 0 ]; then
        if [ "$1" == "sk" ]; then
                TZ='Asia/Seoul' date +"%T"
        fi
    fi
    if [ $# -ne 0 ]; then
        if [ "$1" == "no" ]; then
                TZ='Europe/Oslo' date +"%T"
        fi
    fi
    echo $date ;
    sleep 1 ;
done
