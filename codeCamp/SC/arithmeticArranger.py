import re


def calculate(a, sign, b):
    a = int(a.strip())
    sign = sign.strip()
    b = int(b.strip())

    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b

    return result


def formatter(first_value, sign, second_value, sum=None):
    output_lines = []  # Create an empty list to store formatted lines

    format_length_1 = len(first_value)
    format_length_2 = len(second_value)

    # len grater number + space + sign
    max_index_length = max(format_length_1, format_length_2) + 2

    # 6 is the maximum due to 4 number cipher, space and sign
    first_line = "{:>{}}".format(first_value, max_index_length)
    output_lines.append(first_line)

    second_line = "{}{:>{}}".format(sign, second_value, (max_index_length - 1))  # -1 counting the " "
    output_lines.append(second_line)

    dashes_line = "-" * (max_index_length)
    output_lines.append(dashes_line)

    if sum != None:
        sum_line = "{:{}}".format(sum, max_index_length)
        output_lines.append(sum_line)

    return output_lines


def arithmetic_arranger(problems, value=False):
    # first, look if the list have more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = list()
    for problem in problems:
        # Second, look if there are  * or / operators (if not, index is -1)
        if problem.find("*") != -1 or problem.find("/") != -1:
            return "Error: Operator must be '+' or '-'."
        # Third, look if there are characters different tham integers, "+", "-" or "s = white spaces"
        elif re.search(r'[^0-9\+\-\s]', problem):
            return "Error: Numbers must only contain digits."
        else:
            part = problem.split(" ")
            # fourth, look if there are numbers > 4 digits (0 and 2 substrings)
            if len(part[0]) > 4 or len(part[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
                break
            else:
                if value == True:
                    formatted_lines = formatter(part[0], part[1], part[2], calculate(part[0], part[1], part[2]))
                    # Concatenate the lines from each formatted problem
                else:
                    formatted_lines = formatter(part[0], part[1], part[2], None)
                arranged_problems.append(formatted_lines)

    combined_lines = ""
    # Print the arranged problems in the same line
    for i in range(len(arranged_problems[0])):  # index 0 for watching the elements inside the list
        for problem_lines in arranged_problems:
            combined_lines += problem_lines[i] + "    "
        combined_lines += "\n"

    return combined_lines



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
