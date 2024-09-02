# user_input= ([])      taaask


# def is_valid_parentheses(s):
    
#     matching_pairs = {')': '(', '}': '{', ']': '['}
#     stack = []

#     for char in s:
#         if char in matching_pairs.values():
#             stack.append(char)
#         elif char in matching_pairs.keys():
#             # If the character is a closing bracket, check if it matches the top of the stack
#             if stack == [] or matching_pairs[char] != stack.pop():
#                 return False
#         else:
            
#             continue    # Ignore non-bracket characters

    
#     return stack == []    # If the stack is empty, all opening brackets were properly matched

# input_string = "{[()]}"
# print(is_valid_parentheses(input_string))  # Output: True

# input_string = "{[(])}"
# print(is_valid_parentheses(input_string))  # Output: False

# user_input="[]"
# symbol_table = {'(': ')', '[': ']', '{':'}'}

# symbol_stack=[]
# top=-1
# IsValid=True

# for symbol in user_input:


#     if symbol in symbol_table:

#         top+=1
#         symbol_stack.append(symbol)
        

#     else:

#         if len(symbol_stack)<1:
#             IsValid=False
#             break


#         current_symbol=symbol_stack[top]
#         current_symbol_closing=symbol_table[current_symbol]  #stackle current symbol de closing

#         if symbol==current_symbol_closing:
#             symbol_stack.pop()
#             top=top-1


#         else:

#             IsValid=False
#             break

# if len(symbol_stack)!=0:
#     print(False)
# else:
#     print(IsValid)




user_input="{}"
symbol_stack=[]

symbol_table={"[":"]","{":"}","(":")"}

top=-1

isValid=True
for symbol in user_input:

    if symbol in symbol_table:
        top+=1
        symbol_stack.append(symbol)

    else:

        if len(symbol_stack)>1:
            isValid=False

            break
        current_symbol=symbol_stack[top]
        current_symbol_closing=symbol_table[current_symbol]

        if symbol==current_symbol_closing:
            symbol_stack.pop()
            top-=1

        else:
            isValid=False
            break

if len(symbol_stack)!=0:
    print(False)
else:
    print(True)
    



top=-1

isValid=True
for symbol in user_input:
    if symbol in symbol_table:
        top=top+1
        symbol_stack.append(symbol)

    else:
        len(symbol_stack)>1
        isValid=False
        break
    
        


