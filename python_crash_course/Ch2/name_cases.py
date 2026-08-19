"""Summary line"""

PERSON_NAME = "Yannick"
age = 20

print(
    "Hello " + PERSON_NAME + ", would you like to learn some Python today?" + str(age)
)

print(
    "Hello "
    + PERSON_NAME.title()
    + ", would you like to learn some Python today? "
    + str(age)
)

print("Hello " + PERSON_NAME.upper() + ", would you like to learn some Python today?")

print("Hello " + PERSON_NAME.lower() + ", would you like to learn some Python today?")
