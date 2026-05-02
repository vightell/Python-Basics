# Notes Log

---

## Day 1 — Printing

What I did:
- Learned how to use print()

What I learned:
- Python runs line by line

Problems:
- None

Fix:
- -

---

## Day 2 — Variables

What I did:
- Used variables inside sentences

What I learned:
- Variables store values and can be rreused
Problems:
- Forgot how to format strings

Fix:
- Added quotes correctly

--------

## Day 3 — If / Else

What I did:
- Created basic conditions

What I learned:
- Python checks conditions in order

Problems:
- Indentation errors

Fix:
- Fixed spacing

---

## Day 4 — Lists & Loops

What I did:
- Looped through 5 items

What I learned:
- Loops repeat actions automatically

Problems:
- Mixed up syntax

Fix:
- Corrected loop structure
  
## Day 5 – Loops + State + Git

### Task
Use a for loop to count from 1 to 20.

### What I did
- Implemented the basic loop from 1 to 20
- Extended it to loop far beyond the limit (up to 236)
- Added a secondary variable `j` that:
  - increments by 3
  - resets when it reaches 10
- Added delays using `time.sleep()` to control output speed

### What I learned
- How `range(start, stop)` works
- How loops interact with external variables (state)
- How to create repeating patterns using conditions
- How timing affects program behavior
- How to push code to GitHub using add → commit → push

### Reflection
Started simple, ended up building a looping pattern system.
Took time, but now I understand loops and Git workflow much better.

--------

## Day 6 — Functions

### What I did:
- Created my first function using def
- Passed a name as a parameter into the function
- Printed dynamic output using that parameter
- Fixed indentation to separate definition from execution
- Called the function properly with a string value
- Ran and pushed the working code to GitHub

### What I learned:
- Functions store actions and only run when called
- Parameters are placeholders that receive real values
- Indentation controls what belongs inside a function
- Calling a function triggers its behavior
- Strings ("text") are different from variables

### Problems:
- Forgot the colon (:) after def, causing a syntax error
- Placed the function call inside the function, so nothing executed
- Confused variable vs string when passing the argument
- Terminal showed no output, which was misleading

### Reflection:
At first, the code did nothing and it felt broken.
The issue wasn’t complexity, it was structure and placement.

Once fixed, everything worked instantly.

This day was about control.
Not writing more code, but placing it correctly.

--------
## Day 7 — Mini Project (User Input + Function)

### What I did:
- Built a mini project that asks the user for their name
- Used input() to capture user data
- Created a function greet(name)
- Passed user input into the function
- Printed a personalized greeting message

### What I learned:
- input() allows programs to interact with users
- Functions can take parameters and use external data
- Code becomes reusable when wrapped inside functions
- Programs can feel dynamic instead of static

### Problems:
- Confusion between defining a function and calling it
- Minor syntax and structure errors while testing
- Emotional frustration when things didn’t run instantly

### Reflection:
This was the first time the program responded to *me* instead of just running.
It felt less like writing instructions and more like creating interaction.
The shift from static output to user-output behavior makes the code feel alive.

----------
## Day 8 — Dictionaries

### What I did:
- Created my first dictionary using key-value pairs
- Stored name → age relationships
- Accessed values using keys
- Took user input and stored it inside a dictionary

### What I learned:
- Dictionaries store relationships, not just values
- Keys are used to access specific data
- Data can be added dynamically using input
- Dictionaries are more structured than lists

### Problems:
- Confusion between {} and []
- Remembering to use quotes for keys
- Minor mistakes when accessing values

### Reflection:
Shifted from storing data to organizing meaning.
Code feels more structured, not just sequential.

--------
## Chain Day — I showed up.

--------

## Day 8 — Dictionaries

### What I did:
- Created dictionaries using {}
- Stored key → value pairs (name → age, object → meaning)
- Took user input and saved it inside a dictionary
- Accessed values using keys (dict[key])
- Built multiple dictionary examples (squad, sky, human)
- Iterated through a dictionary using a loop

### What I learned:
- {} creates a dictionary (key-value structure)
- dict[key] = value assigns data dynamically
- Keys are unique identifiers used to retrieve values
- Dictionaries model relationships, not just data
- Looping through a dictionary allows structured output

### Problems:
- Confusion between [] and {}
- Syntax errors while creating dictionaries
- Misunderstood how dict[key] = value works at first
- Needed help initially, then gradually became independent

### Reflection:
Started confused about what a dictionary even is.
Ended up creating multiple versions from scratch with decreasing help.
Understanding shifted from “random syntax” to “mapping relationships.”
Still not perfect—but no longer unfamiliar.

--------

## Day 9 — Looping Through Dictionaries

### What I did:
- Created a dictionary with key-value pairs (individual → trajectory)
- Used a loop to go through the dictionary
- Printed both key and value together in a readable sentence
- Practiced `.items()` to access key and value at the same time
- Improved naming (individual, role) instead of generic names

### What I learned:
- A dictionary stores relationships (key → value), not just data
- `for key in dict:` loops through keys only
- `dict[key]` is used to access the value of that key
- `.items()` returns both key and value together
- `for key, value in dict.items()` is the cleanest way to read both sides
- Looping + dictionaries = structured output, not random prints

### Problems:
- Confusion between looping keys vs looping key-value pairs
- Needed repetition to understand `dict[key]`
- Slight hesitation with syntax and structure

### Reflection:
This wasn’t just looping.
It was reading relationships.

Instead of printing isolated values,
I started printing meaning.

The code now describes something,
not just executes.

--------
## Day 10 — Filtering with Lists + Loops + Conditions

### What I did:
- Revisited the concept for the third time to strengthen understanding
- Created a list of items (zoo)
- Used a for loop to iterate through each element
- Applied if / elif / else conditions inside the loop
- Used len() to evaluate each item
- Built a simple classification system based on rules

### What I learned:
- Lists store multiple values in one structure
- Loops allow me to process each item automatically
- Conditions inside loops create filtering logic
- len() can be used to analyze data (like string length)
- Code can evaluate and classify data, not just print it

### Problems:
- Logical rules were arbitrary (based only on length)
- Realized conditions can work but still be meaningless
- Slight confusion between creative logic vs useful logic

### Reflection:
This was my third time engaging with this concept, and it became clearer through repetition.
Instead of just running code, I made it decide and classify.
Even if the logic was simple, it showed me how code can filter reality.

---------

## Day 11 — Functions with Logic

### What I did:
- Created my first function using def
- Used input() to take user data (name + level)
- Converted input to integer using int()
- Built conditional logic inside a function (if / elif / else)
- Called the function to execute it
- Combined identity logic (name check) with numeric evaluation (level system)

### What I learned:
- def creates a reusable block of code (a system, not just lines)
- Functions don’t run unless you call them
- input() always returns a string → must convert to int() for numbers
- Conditions inside functions behave the same as outside
- Order of conditions matters (top-down execution)
- You can separate logic (name vs level) into different decision layers

### Problems:
- Forgot indentation after defining function
- Tried invalid syntax for ranges (level = (50-100))
- Confused function parameters vs input inside function
- Logic flow was mixed (name + level interfering)
- Syntax errors from missing colons or incorrect comparisons

### Reflection:
Started chaotic, full of syntax errors and confusion.
Ended with a working system that takes input, processes identity, and evaluates status.

This wasn’t just “functions.”
This was my first step into building structured decision systems.
