
automate

given: date, current 'value', pay rate (weekly, bi-weekly, bi-monthly)
show: Year-end value

example:

$1 on 2020-01-07, weekly : Year-end: $52
$1 on 2020-01-14, bi-monthly : Year-end: $24
$1 on 2020-01-07, bi-weekly : Year-end: $26

alternate 2:
given:
    current week (default 1 )
    current value (default 0)
    goal (default = 0 ) 

    calculate: needed addition (Contribution) to get to goal in remaining weeks.
    Assuming goal is Year End, so week = 52

#   Running
# Build docker, then run it:
docker build -t foobar .
docker run -it foobar 

#   Just run it:
docker run -it --rm --name foobar1 -v $PWD:/foob  python python /foob/bin/calc_401k_contrib.py
