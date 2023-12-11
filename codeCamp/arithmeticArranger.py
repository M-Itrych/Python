import re

def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

    for problem in problems:
        if re.search("[^\\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                return "Error: Operator must be '+' or '-'."

            return "Error: Numbers must only contain digits."

        firstNumber = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        secondNumber = problem.split(" ")[2]

        if len(firstNumber) >= 5 or len(secondNumber) >= 5:
            return "Error: Number cannot be more than four digits."

        sum = ""

        if operator == "+":
            sum = str(int(firstNumber) + int(secondNumber))
        elif operator == "-":
            sum = str(int(firstNumber) - int(secondNumber))

        length = max(len(firstNumber), len(secondNumber))
        top = str(firstNumber).rjust(length + 6)
        bottom = (operator + " " + str(secondNumber)).rjust(length + 6)
        line = ""
        res = str(sum).rjust(length)

        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first += top
            second += bottom
            lines += "    " + line
            sumx += res
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

        if answer:
            string = first + "\n" + second + "\n" + lines + "\n" + sumx
        else:
            string = first + "\n" + second + "\n" + lines

    return string




print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))