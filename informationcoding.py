# -*- coding: utf-8 -*-

import numpy as np
#from libgf2.gf2 import checkPeriod, GF2QuotientRing

def binary_polynomial(n:int, width:int):
    binary = np.binary_repr(n,width)
    poly = ''
    bitlength = 0
    poly_array = np.zeros(width)
    for i in range(width-1,0,-1):  # binary representation is big endian (msb on left)
        if binary[i] == '1':
            bitlength = width - i  #
        poly += str(binary[i]) + '*x^' + str(width - i)
        poly_array[width - i - 1]= binary[i]
        if i != 1:
            poly += ' + '
    return (binary, poly,poly_array, bitlength)


def nary_polynomial(n:int, width:int, base:int):
    nary = np.base_repr(n, base, width)
    #print(nary)

def get_coefficients_powers(poly:str):
    coeff = poly.split('*')[0]
    power = poly.split('^')[1]
    return(coeff,power)
