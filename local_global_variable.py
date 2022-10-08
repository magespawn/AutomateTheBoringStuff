spam = 42 # global variable called when the program runs and destroyed when the program ends.

def eggs():
    global eggs # global statement.
    spam = 42 # local variable created when the functions is called and destroyed when the function ends.

print('Some code here.')
print('Some more code here.)
      # 1. Code in the global scope cannot use any local variables.
      # 2. Code in local scope can access global variables.
      # 3. Code in one function's local scope cannot use variables in another local scope.
      # 4. You can use the same name for variables as long as they are in different scopes.
