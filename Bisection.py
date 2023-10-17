import csv
import math
import re



def Bisection(file):
    print("\nprinting from bisection:\n", file.read().strip())
    pass


def Newton(file):
    '''TODO: implement logic'''
    print("newt")




def Secant(file):
    '''TODO: implement logic'''
    print("sec")


def Hybrid(file):
    '''TODO: implement logic'''
    print("hybrid")




if __name__ == '__main__':
    #taking in user input, splitting it, and picking out necessary info
    raw_inp = (str(input("\nPlease enter input in the following order"))).split(" ")
    try:
        with open(raw_inp[-1], 'r') as file:
            if re.search("-newt", raw_inp[1]):
                Newton(file)
            elif re.search("-sec", raw_inp[1]):
                Secant(file)
            elif re.search("-hybrid", raw_inp[1]):
                Hybrid(file)
            else:
                Bisection(file)
    except FileNotFoundError as err:
        print(err)


