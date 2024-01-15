def add(x:int,y:int):
    return x+y

def subtraction(x:int,y:int):
    return x-y

def multiplication(x:int,y:int):
    return x*y

def division(x:int,y:int):
    return x/y


def long_number_check(expression:str,start_index:int):
    end_index = start_index
    while end_index < len(expression) and expression[end_index].isdigit() == True:
        end_index+=1
    return start_index+1 if start_index == end_index else end_index


def expression_to_list(expression:str):
    expression_list = []
    i=0
    negetive_number = False
    while i < len(expression):
        end_index = long_number_check(expression,i) #the end index is not part of the number
        if negetive_number == True :
            expression_list.append("-"+expression[i:end_index])
            negetive_number = False
            i = end_index
            continue
        if i == 0 and expression[i] == "-": #check if the first number is negetive
            negetive_number = True
            i = end_index
            continue
        if (expression[i] == "/" or expression[i] == "*" or expression[i] == "+") and expression[i+1] == "-" :
            expression_list.append(expression[i])   
            negetive_number = True
            i=i+2
        else:
            expression_list.append(expression[i:end_index])
            i = end_index
    return expression_list


def string_to_digit(expression_list_str:list[str]):
    digit_list = []
    for char in expression_list_str:
        if  char.strip("-").isdigit() == True:
            digit_list.append(int(char))
        else:
            digit_list.append(char)

    return digit_list


def calculate_list_helper_mult_div(math_exp:list,counter:int,op:str):
    sum = 0
    while counter > 0:
        index = math_exp.index(op)
        if op == "*":
            sum = multiplication(math_exp[index-1],math_exp[index+1])
        if op == "/":
            sum = division(math_exp[index-1],math_exp[index+1])
        math_exp[index-1] = sum
        math_exp.pop(index+1)
        math_exp.pop(index)
        counter-=1


def calculate_list_helper_add_sub(math_exp:list):
    sum = 0 
    index = 0 
    while index < len(math_exp):
        if math_exp[index] == "+":
            sum = add(math_exp[index-1],math_exp[index+1])
        elif math_exp[index] == "-":
            sum = subtraction(math_exp[index-1],math_exp[index+1])
        else:
            index+=1
            continue
        math_exp[index-1] = sum
        math_exp.pop(index+1)
        math_exp.pop(index)
    
    
def calculate_list(math_exp:list):
    mult_and_div = ["*","/"]
    for op in mult_and_div:
        counter = math_exp.count(op)
        calculate_list_helper_mult_div(math_exp,counter,op)
    calculate_list_helper_add_sub(math_exp)
    return math_exp[0]


def main_calculator():
    targil = input("Enter math exercise: ")
    targil = targil.replace(" ","")
    targil = expression_to_list(targil)
    targil = string_to_digit(targil)
    ans = calculate_list(targil)
    return ans



if __name__ == "__main__":
    print(main_calculator())