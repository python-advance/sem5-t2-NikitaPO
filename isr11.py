def get_fib_nums_lst(n):
    """
    n - количество чисел в списке 

    """
    if ((type(n) == str) or (n <= 0)): 
      return None

    fib_list = [0]
    first = 0
    middle = 1
    while(n > 1): 
      fib_list.append(middle)
      third = first + middle
      first = middle
      middle = third
      n -= 1

    return fib_list
