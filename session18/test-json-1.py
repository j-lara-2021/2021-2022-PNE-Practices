import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-3.json").read_text()

# Create the object person from the json string
# .loads(file) creates a dictionary from the json file
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# -- Read the Firstname
firstname = person['Firstname']
lastname = person['Lastname']
age = person['age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(firstname, lastname)
termcolor.cprint("Age: ", 'green', end="")
print(age)