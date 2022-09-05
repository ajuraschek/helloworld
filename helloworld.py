#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Hello World Program'

__author__ = 'Andrew Juraschek' #code drawn from https://www.code-learner.com/python-module-introduction/

import sys

def say_hello():
    args = sys.argv
    if len(args)==1:
       print('Hello, World!')
    elif len(args)==2:
       print('Hello, %s!' % args[1])
    else:
       print('Too many arguments!')

if __name__=='__main__':
     say_hello()