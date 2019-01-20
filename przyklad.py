#! /usr/bin/python

def f1(x,y=0):
    if y==0:
        if x<=1:
            return x
        else:
            return x*x
    else:
        if x<=1:
            return x +y
        else:
            return x*x +y
