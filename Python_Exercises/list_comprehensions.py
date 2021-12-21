# List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.

temps = [221, 220, 330, 450]

new_temps = []

# A very manual way of doing list comprehension would be:
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

# We can shorten this using list comprehension:
new_temps = [temp/10 for temp in temps]

print(new_temps)

# List comprehension with conditionals:
new_temps = [temp/10 for temp in temps if temp > 300]

print(new_temps)

# For if-else conditions, the syntax is a little different with the 'for' section
# coming in last
new_temps = [temp/10 if temp > 300 else 0 for temp in temps]

print(new_temps)
