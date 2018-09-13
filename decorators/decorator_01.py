# -*- coding: utf-8 -*-
def f1(f):
    def fx():
        print("this is before calling")
        f()
        print("this is after calling")
    return fx


@f1
def f3():
    print("this is from f3()")


f3()
