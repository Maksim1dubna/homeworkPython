def apply_all_func(int_list, *functions):
    functions = functions
    for func in functions:
        func(int_list)
    return 0

def max_list(int_list):
    print(f"max: {max(int_list)}")
def min_list(int_list):
    print(f"min: {min(int_list)}")
def summ(int_list):
    print(f"Summ:{sum(int_list)}")

apply_all_func([6, 20, 15, 8], max_list, min_list, summ)