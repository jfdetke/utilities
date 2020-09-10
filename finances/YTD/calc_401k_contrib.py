#!/usr/bin/env python3
'''
utility to compute needed contribution to max out my 401k.
Defaults are for the year, e.g. weekly contrib to hit my max:$26k

Future work:
    given current week, and current value, calc necessary weekly contrib to hit max.
    This was to help adjust Lisa's, who's income varies a bit

    also, some contrib's are percent based, would be nice to calc that. That would
    require another param: income
'''
def calc_week(now=0):
    '''
    function to calculate the current week, given (the current time? date?)
    '''
    return(1)   # For now, its always the first week

def calc_contrib(myweek=1,myvalue=0,mygoal=0):
    print("calc'ing contribution")
    my_contribution = 0
    my_contribution = mygoal
    end_week = 52   #   default to Year End
    time_left = end_week - myweek
    print(time_left,"weeks left")


    my_contribution = ( mygoal - myvalue )  / time_left
    print("Contribute: ", my_contribution, "to reach", mygoal, " in",time_left,"weeks")

def main():
    foob=42
    foob = calc_week()
    print("This is weeek:",foob)
    calc_contrib(37,10300,26000)


if __name__ == "__main__":
    main()
