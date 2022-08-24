customer = {
    "name": "prashant vaghani",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "13 march 1998"
print(customer["birthdate"])


phone = input("phone: ")
digital_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digital_mapping.get(ch, "!") + " "
print(output)


message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

def greet_user():
    print("hello")
    print("welcome to our island")

print("start")
greet_user()
print("finish")

