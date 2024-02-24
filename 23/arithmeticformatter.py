def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def calculate_result(formatted_problems):
    results = []
    for problem in formatted_problems:
        num1, operator, num2 = problem
        num1, num2 = int(num1), int(num2)
        result = num1 + num2 if operator == '+' else num1 - num2
        results.append(result)
    return results

def arithmetic_arranger(problems, show_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    formatted_problems = []
    for problem in problems:
        num1, operator, num2 = problem.split()
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not is_number(num1) or not is_number(num2):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        formatted_problems.append((num1, operator, num2))

    line1 = ""
    line2 = ""
    dashes_line = ""
    results_line = ""

    for num1, operator, num2 in formatted_problems:
        width = max(len(num1), len(num2)) + 2
        line1 += num1.rjust(width) + '    '
        line2 += operator + ' ' + num2.rjust(width - 2) + '    '
        dashes_line += '-' * width + '    '

    arranged_problems = f"{line1.rstrip()}\n{line2.rstrip()}\n{dashes_line.rstrip()}"

    if show_result:
        results = calculate_result(formatted_problems)
        results_line = ""
        for result in results:
            width = len(str(result)) + 2
            results_line += str(result).rjust(width) + '    '

    return f"{arranged_problems}\n{results_line.rstrip()}" if show_result else arranged_problems
