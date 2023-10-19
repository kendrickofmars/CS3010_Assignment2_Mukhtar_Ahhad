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
        init_p = inp[3]
        init_p2 = inp[4]
    else:
        init_p = inp[2]
        init_p2 = inp[3]
        max_iter = 10000

    print("Max number of iterations is: {}".format(max_iter))
    '''In Bisection, we have 2 initial points, a and b. init_p and init_p2 hold the starting values in the input string that 
        the user sends in. They are our starting values which we will find a zero between. 
        We will plug these into our function, so we can find the difference between f(a) and f(b)'''

    print("a = {} and b = {}".format(init_p,init_p2))

    '''Next, we need to parse our file contents properly. This means recognizing the coefficients in the file and 
      setting the exponents to decrease from a maximum value of 3. '''


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


