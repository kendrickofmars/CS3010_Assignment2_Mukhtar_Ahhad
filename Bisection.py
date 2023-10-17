import csv
import math
import re



def Bisection(file, inp):
    '''Input is organized in the following manner:
    "polRoot [-newt, -sec, -hybrid] [-maxIt n] initP [initP2] polyFileName"
    our maximum number of iterations will be set to whatever follows the -maxIter keyword, otherwise default val is 10k
    '''
    if re.search("-maxIter", inp[1]):
        max_iter = inp[2]
    else:
        max_iter = 10000

    print("Max number of iterations is: {}".format(max_iter))

    '''Next, we need to get the starting values to find a zero between. In Bisection, we have 2 initial points, 
       a and b. We will plug these into our function, so we can find the difference between f(a) and f(b)'''


def Newton(file, inp):
    '''TODO: implement logic
    :param inp:
    '''
    print("newt")




def Secant(file, inp):
    '''TODO: implement logic
    :param inp:
    '''
    print("sec")


def Hybrid(file, inp):
    '''TODO: implement logic
    :param inp:
    '''
    print("hybrid")


def main():
    '''taking in user input, splitting it, and picking out necessary info'''
    raw_inp = (str(input("\nPlease enter input in the following order:\n"
                         "polRoot [-newt, -sec, -hybrid] [-maxIter n] initP [initP2] polyFileName\n"
                         "Input is case sensitive and order-dependent. \n"))).split(" ")
    try:
        with open(raw_inp[-1], 'r') as file:
            if re.search("-newt", raw_inp[1]):
                Newton(file, raw_inp)
            elif re.search("-sec", raw_inp[1]):
                Secant(file, raw_inp)
            elif re.search("-hybrid", raw_inp[1]):
                Hybrid(file, raw_inp)
            else:
                Bisection(file, raw_inp)
    except FileNotFoundError as err:
        print(err)
        main()


if __name__ == '__main__':
    main()


