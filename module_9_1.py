def apply_all_func(int_list, *functions):
    results = {}

    for fun_name in functions:
        __name__= fun_name
        results[fun_name.__name__] = __name__(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))