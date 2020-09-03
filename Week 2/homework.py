import logging
logging.basicConfig(level=logging.DEBUG)
def squared_threes():
    return_value = list(range(3,100,3))
    return_value = [values ** 2 for values in return_value]
    return return_value
if __name__ == "__main__":
   for x in squared_threes():
       print(x)
   # should print out all numbers between 0 and 99 (inclusive)
   # that are evenly divisible by 3, then squared.
   # e.g 
   # 9
   # 36
   # 81 
   # .....   etc