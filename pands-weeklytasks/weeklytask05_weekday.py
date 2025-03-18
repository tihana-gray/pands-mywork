# Program that outputs whether or not today is weekday.
# Author: Tihana Gray

from datetime import datetime

def main():
    # Tuples to store weekdays and weekends
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    weekends = ("Saturday", "Sunday")

    # Dictionary mapping numbers to day names
    day_map = {
        0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday",
        5: "Saturday", 6: "Sunday"
    }

    # Get the current day as an integer (0=Monday, ..., 6=Sunday)
    today_num = datetime.now().weekday()

    # Get the actual day name using the dictionary
    today_name = day_map[today_num]

    # Use a set to check if today is a weekday or weekend
    if today_name in set(weekdays):
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")

if __name__ == "__main__":
    main()