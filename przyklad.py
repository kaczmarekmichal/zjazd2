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
def f2(x):
    if len(x)>0:
        return x[0]
    else:
        return "BUUUM"
