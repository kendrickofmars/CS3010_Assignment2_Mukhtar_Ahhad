import csv
import math
import re
import itertools

'''We read in the split file, and replace double spaces with single-spaces, which we then use as our delimiter.
    This allows us to get each numerical value to be it's own list item. From there we use the itertools module to
    concatenate the list of lists "line" into a singular list which contains all the values we need.'''


def file_parser(file, raw_inp):

    #List comprehension to get each line in the file, this is slightly more efficient than a regular for loop.
    line = [x.replace("  ", " ").split(r" ") for x in file]
    value_list = list(itertools.chain.from_iterable(line))

    n = value_list[0]  # first value in the list is the higest degree for our polynomial
    const = value_list[-1]  # constant term is always the last value of our list
    max_iter = 10000 #default max iteration value if none specified
    epsilon = 2e-23 #error tolerance


    if re.search("-newt", raw_inp[1]):
        if re.search("-maxIter", raw_inp[2]):
            '''If we specify max iterations, our init_p @ index 4'''
            max_iter = raw_inp[3]
            init_p = raw_inp[4]  # a
            newton(value_list, raw_inp, n, const, init_p, max_iter,epsilon)
        else:
            '''No "-maxIter" :keyword or :param max_iter? ==> init_p @ index 2'''
            init_p = raw_inp[2]
            newton(value_list, raw_inp, n, const, init_p, max_iter,epsilon)

    elif re.search("-sec", raw_inp[1]):
        if re.search("-maxIter", raw_inp[2]):
            '''If we specify max iterations, our initial zeros a and b are at values 4 and 5 of our list respectively'''
            max_iter = raw_inp[3]
            init_p = raw_inp[4]  # a
            init_p2 = raw_inp[5]  # b
            secant(value_list, raw_inp, n, const, init_p, init_p2, max_iter)
        else:
            '''No "-maxIter" :keyword or :param max_iter? ==> init_p & init_p2 located at index 3 and index 4 respectively'''
            init_p = raw_inp[2]
            init_p2 = raw_inp[3]
            secant(value_list, raw_inp, n, const, init_p, init_p2, max_iter)

    elif re.search("-hybrid", raw_inp[1]):
        #hybrid starts with bisection for earlier iterations and then switches to Newton's method
        hybrid(value_list, raw_inp)

    else:
        if re.search("-maxIter", raw_inp[1]):
            '''If we specify max iterations, our initial zeros a and b are at values 2 and 3 of our list respectively'''
            max_iter = raw_inp[2]
            init_p = raw_inp[3]  # a
            init_p2 = raw_inp[4]  # b
            bisection(value_list, raw_inp, n, const, init_p, init_p2, max_iter, epsilon)
        else:
            '''No "-maxIter" :keyword or :param max_iter? ==> init_p & init_p2 located at index 1 and index 2 respectively'''
            init_p = raw_inp[1]
            init_p2 = raw_inp[2]
            bisection(value_list, raw_inp, n, const, init_p, init_p2, max_iter, epsilon)
    # print("Printing lines from the file", value_list)
    return value_list


'''Input is organized in the following manner:
    "polRoot [-newt, -sec, -hybrid] [-maxIt n] initP [initP2] polyFileName"
    our maximum number of iterations will be set to whatever follows the -maxIter keyword, otherwise default val is 10k
    '''
def fa(init_p):
    '''TODO: implement logic here'''

    return 0


def fb(init_p2):
    '''TODO: implement logic here'''
    return 0
def bisection(value_list, inp, n, const, init_p, init_p2, max_iter, epsilon):
    f_init_p = fa(init_p)
    f_init_p2 = fb(init_p2)
    '''for i in range(len( we will add terms of the polynomial to one another. So from 1:-1, we would add
    coeff[i]*init_p^(n-(i-1)) + coeff[i+1]*init_p^(n-(i-1)) + coeff[i+2]*init_p^(n-(i-1)) + '''
    '''In Bisection, we have 2 initial points, a and b. init_p and init_p2 hold the starting values in the input string that 
        the user sends in. They are our starting values which we will find a zero between. 
        We will plug these into our function, so we can find the difference between f(a) and f(b)'''

    print("Max iterations = {}, a = {} and b = {}".format(max_iter, init_p, init_p2))

    '''Next, we need to parse the values of the list properly. 
    value_list format:n, a(n) a(n-1) a(n-2) ... a(2) a(1) const 
    This means that the first value in the value_list is:
     n- degree of the polynomial
     a(i) - coefficient of the monomial of the degree i
     const- constant term'''

    print("Printing lines from the file in bisection method: ", value_list)

    print("f(init_p) = {}".format(f_init_p))
    print("f(init_p2) = {}".format(f_init_p2))
def newton(value_list, raw_inp, n, const, init_p, max_iter, epsilon):
    '''TODO: implement logic
    :param raw_inp
    :param value_list '
    :param: n
    :param: const
    :param init_p
    :param max_iter
    :param epsilon'''
    print("Max iterations = {}, a = {}".format(max_iter, init_p))
    print("Printing lines from the file in Newton's method: ", value_list)


def secant(value_list, raw_inp, n, const, init_p, init_p2, max_iter):
    '''TODO: implement logic
    :param raw_inp
    :param value_list '
    :param: n
    :param: const
    :param init_p
    :param init_p2
    :param max_iter'''
    print("Max iterations = {}, a = {} and b = {}".format(max_iter, init_p, init_p2))
    print("Printing lines from the file in secant method: ", value_list)


def hybrid(value_list, inp):
    '''TODO: implement logic
    :param inp:
    :param value_list - correctly formatted list
    '''
    print("hybrid")


def main():
    '''taking in user input, splitting it, and picking out necessary info'''
    raw_inp = (str(input("\nPlease enter input in the following order:\n"
                         "polRoot [-newt, -sec, -hybrid] [-maxIter n] initP [initP2] polyFileName\n"
                         "Input is case sensitive and order-dependent. \n"))).split(" ")
    try:
        with open(raw_inp[-1], 'r') as file:
            '''Calling file parser to take the raw input from user so we can then call each method based on what the user entered.
                We also pass in the file list object that we split input in using a newline delimiter.'''
            file = file.read().split("\n")
            file_parser(file, raw_inp)

    except FileNotFoundError as err:
        print(err)
        main()


if __name__ == '__main__':
    main()


