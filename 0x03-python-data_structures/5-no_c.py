def no_c(my_string):
    for _ in my_string:
        if _ not in ['c', 'C']:
            print(_, end="")
    print()
