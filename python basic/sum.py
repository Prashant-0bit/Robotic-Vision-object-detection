prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total:  {total}")

# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2050  # year
  # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.calendar(yy))
