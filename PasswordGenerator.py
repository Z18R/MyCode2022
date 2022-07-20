import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIPKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symblos = "!@#$%^&*()_+"

string = lower + upper + numbers + symblos
lengeth = 12
password = "".join(random.sample(string,lengeth))

print("Your new Password is: " + password)