import re

def arithmetic_arranger(problems, solve = False):
    table = [[],[],[],[]]
    arranged_problems = ""

    if len(problems) > 5:
        print("Error: Too many problems.")
        return "Error: Too many problems."
    for idx,arg in enumerate(problems):
        error1 = re.search("[a-zA-Z]",arg)
        if error1 != None: 
            print("Error: Numbers must only contain digits.")
            return("Error: Numbers must only contain digits.")

    for idx,arg in enumerate(problems):
        first = re.search("^\d+",arg).group()
        operator = re.search("(\+|-|\*|/)",arg).group()
        last = re.search("\d+$",arg).group()
        if operator is "*" or operator is "/":
            print("Error: Operator must be '+' or '-'.")
            return("Error: Operator must be '+' or '-'.")
        if len(first) > 4 or len(last) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return("Error: Numbers cannot be more than four digits.")
        ans = str(eval(first + operator + last))
        spacing = 1 if len(last) >= len(first) else abs(len(first) - len(last)) + 1 
        table[1].append(operator + " "*spacing + last)
        table[0].append(" " * (len(table[1][idx])-len(first)) + first)
        table[2].append("-" * len(table[1][idx]))
        table[3].append(" " * (len(table[2][idx]) - len(ans)) + ans)
        
    if solve is False:
        table.remove(table[3])
    for idx1,row in enumerate(table):
        for idx2, x in enumerate(row):
            arranged_problems += (x + "    ") if idx2 + 1 < len(row) else x
        arranged_problems += "\n" if idx1 + 1 < len(table) else ""


    print(arranged_problems)
    return arranged_problems
