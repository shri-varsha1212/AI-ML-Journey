#organizing code with functions. 
# function is a block of code designed to perform a specific task. 
#functions will let you do roughly the ssme calculation multiple times without creating a duplicate in the code
# first step is todefine the fuction
def add_three(input_var)
    output_var=input_var+3
    return output_var
#here the return function exits from the code
#a function can have no arguments or multiple argument
new_no= add_three(10)
print(new_no)
#here the output is 30
#variables inside the function body cannot be accessed outside of the function

# functions with multiple arguments
