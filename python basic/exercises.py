def sum_thrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

def larger_string(str, n):
   result = ""
   for i in range(n):
      result += str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y\%m\%d %H:%M:%S"))
