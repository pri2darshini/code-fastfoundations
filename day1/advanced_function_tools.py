import random
import sys


def double_number(n):
    return 2 * n


def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(double_number, random_numbers) = }")


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{list(filter(lambda w: len(w) > 7, words) )= }")

def my_dictionary(my_dict):

    result_dict = dict()  # create a new dictionary
    for key,values in my_dict.items():
        result_dict[key] = values * values
    return result_dict





    print (f"{my_dict=}")

def main():
    #using_map()
    #using_map_and_lambda()
    #using_filter()
    my_dict = {'a': 1,
               'b': 2,
               'c': 3
               }
    sqr_dict = my_dictionary(my_dict)
    filtered_dict = filter(lambda v: 70 < v <100, sqr_dict.values)
    return 0


if __name__ == '__main__':
    sys.exit(main())
