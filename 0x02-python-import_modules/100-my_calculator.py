#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    op_list = ['+', '-', '*', '/']
    op_func = [add, sub, mul, div]
    if operator not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    curr_idx = -1
    for idx, op in enumerate(op_list):
        if op == operator:
            curr_idx = idx
            break
    print("{} {} {} = {}".format(a, operator, b, op_func[curr_idx](a, b)))
