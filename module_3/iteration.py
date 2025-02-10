# Iteration in Python

# For loops are 'for each' loops with no index referenced

# For loop with index in other languages:
# for (var i = 0; i < arr.length; i++) {
#     var value = arr[i];
#     alert(i + ") " + value);
# }

# Python for loop

for character in "A string":
    print(character)

# If you need an index, use enumerate builtin

for index, character in "A string":
    print(index, character, end=" ")

# Use range to do something a certain number of time, indicate with _ convention if you don't use the number

for _ in range(5):
    print("#")

# Loops do not create a local namespace. Will modify global variables. Be careful with naming in for loop

var = 1

for var in range(3):
    print(var)

print(var)

# Loop control with break and continue

for num in range(100):
    print(num)
    if num > 10:
        break

for num in range(100):
    if num > 50:
        break
    if num < 25:
        continue
    print(num)

# For loops can have an else block that executes if the loop exits normally (no break)

for num in range(10):
    print(num)
else:
    print("That's all folks!")

for num in range(10):
    if num == 5:
        print(num)
        break
else:
    print("That's all folks!")

# While loops - exit infinite loop with control-C

some_condition = True

while some_condition:
    print("Repeat me")

# While loops need an exit condition to evaluate to False. You can create a boolean 'flag' variable

looping = True
count = 0

while looping:
    count += 1
    if count > 10:
        looping = False
    print(count)

# Exit while loop with break

count = 0

while True:
    count += 1
    print(count)
    if count > 10:
        break

# Exit while loop with conditional statement in loop

count = 0

while count < 10:
    count += 1
    print(count)
