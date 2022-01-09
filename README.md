# A basic Python Tkinter Calculator with UX improvements
A semi-advanced calculator built using tkinter in python.

Function buttons:

# Delete
Deletes the last character in a string. Can be reversed (once)

# Clear
Clears the entire field. Can be reversed.

# Back
Will go back to the previous state. This rolls back changes made by 
- Delete (1 character is remembered, so only the most recent deletion)
- Clear (will restore the cleared string)
- Equals (will go back to the expression)
- Math functions - soft green colored buttons (will go back to the expression)
