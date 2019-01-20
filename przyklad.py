#! /usr/bin/python
import re

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

def f3(x):
    if x<=3:
        if x==1:
            return "jeden"
        if x==2:
            return "dwa"
        if x==3:
            return "trzy"
    else:
        return "other"

def f4(x ,y=""):
    if len(y)==0:
        return x+ " ma kota"
    else:
        return x+ " ma kota i "+y

def f5 (x, y=0):
    tablica = []

    if y==0:

        if x==0:
            return []
        if x==1:
            return [x-1]
        if x>1:
            for a in range (x):
                tablica.append(a)
            return tablica
    if y>1:
        for a in range (x/y+1):
            tablica.append(a*y)
        return tablica

def f6(x):
    return "*"*x


# refactor code with regualar expressions only!
def f7(x):
    if isinstance(x, str):
        if re.search(" ",x):
            return "zdanie"
        else:
            if re.search("</",x):
                    return "tag koncowy"
            if re.search("<",x):
                    return "tag poczatkowy"
        return "slowo"
    if isinstance(x, int):
        if 0<=x<10:
            return "cyfra"
        else:
            if x<0:
                return "liczba ze znakiem"
            else:
                return "liczba"

def f8(x, y):
    if re.search(x,y):
        return True
    else:
        return False

def f9(x,y):
    if x>0 and y>0:
        return "dodatnie"
    if x<0 and y<0:
        return "ujemne"
    if (x>0 and y<0) or (x<0 and y>0):
        return "roznych znakow"
    if x==0 or y== 0:
        return "zero"
    if x==y:
        return "rowne"
    if x!=y:
        return "rozne"


def f10(x,y):
    if x==y:
        return "rowne"
    if x!=y:
        return "rozne"
