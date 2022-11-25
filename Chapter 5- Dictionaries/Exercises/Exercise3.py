## Exercise 3: Glossary 2

glossary = {'Variable':'let\'s you store a value by assigning it to a name.','Boolean':
             'which allows us to combine multiple conditions.','Concatenation':'To append one string to the end of another string.',
             'Comments':'notes of explanation within a program.', 'Loops':'repeat a block of code multiple times.','List':'used to store items.',
             'Integers':'whole number called integers.','Strings':'text enclosed in single or double quote.',
             'Break':'to end a while loop prematurely.','Input':'any data that the program receives while it is running'}


for word, definition in glossary.items():
    print("\n" + word + ": " + definition)
    