# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
# Reference from where the code was taked/learned 
# Python3 code to Check for 
# balanced parentheses in an expression
open_list = ["[","("]
close_list = ["]",")"]
  
# Function to check parentheses
def Parentesis(problem):
    stack = []
    for i in problem:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Incorrect Syntax"
    if len(stack) == 0:
        return "Correct Syntax"
    else:
        return "Incorrect Syntax"
  
  
# Driver code
string = '()'
print(string,"-", Parentesis(string))
  
string = '()()()()()()()()()'
print(string,"-", Parentesis(string))
  
string = '([])[]()'
print(string,"-",Parentesis(string))

string = ')'
print(string,"-",Parentesis(string))

string = '()['
print(string,"-",Parentesis(string))

string = '(([))]'
print(string,"-",Parentesis(string))

string = '(((((((((((((((((((((((((((((((((('
print(string,"-",Parentesis(string))
