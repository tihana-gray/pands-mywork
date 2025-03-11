# Tuple that stores the months of the year
# from that tuple creating another tuple with just summer months
# printing out summer months one at a time.

# Author: Tihana Gray

months =("January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December")

summer = months[4:7]
for month in summer:
    print(month)