
def fibo_count(ctr):
    '''
    Produces a fibonacci sequence.
    '''
    start = 2
    initial_list = [0, 1]

    while start < ctr:
        initial_list.append(initial_list[-2] + initial_list[-1])
        start += 1
    
    return initial_list

print(fibo_count(10))