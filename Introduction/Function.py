def is_leap(year):
    
    # Write your logic here
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input())