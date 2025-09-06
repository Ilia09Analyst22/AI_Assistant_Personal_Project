#!/bin/bash
greet="Hello, how can I help you?"
x="Yes"
if [ $x -eq "Yes"]; then
    echo $greet
fi
accepted_queries=("Weather" "Python" "Time" "NASDAQ" "DOW" "Stock" "Canadian dollar")
user_request=""

check_query() {
    local q=$(($1))
    if $user_request -eq $q; then
        echo "Yes"
    else
        echo "No"
    fi
}
in_queries() {
    for query in $accepted_queries; do
        $(check_query $query); done
}

is_in_queries=$(in_queries)
if [ $is_in_queries -eq "Yes" ]; then
    continue
else
    kill
fi

execute() {
    if [ $user_request -eq "Weather"]; then
        echo "The weather is quite fine"
    elif [ $user_request -eq "Python"]; then
        echo "Python is a modern programming language used for all purposes"
    elif [ $user_request -eq "Time"]; then
        echo "I don't know what time it is. I will check for you (please run python)"
    elif [ $user_request -eq "NASDAQ"]; then
        echo "I will check using Python's yfinance library"
    elif [ $user_request -eq "DOW"]; then
        echo "I will check using Python's yfinance library"
    elif 
        echo "I will check using Python's yfinance library"
    elif 
        echo "I will check using Python's yfinance library"
    else
        echo "It seems that you entered an invalid request"
}
for i in $accepted_queries;
    do execute(); done

