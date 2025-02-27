# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V7supobcXfATDcweGVZJ3eaM-_o5o1A-
"""

import numpy as np

def FizzBuzz(start, finish):
    FizzBuzz = np.arange(start, finish + 1)

    mod3 = FizzBuzz % 3 == 0
    mod5 = FizzBuzz % 5 == 0

    result = FizzBuzz.astype(str)

    result = np.where(mod3 & mod5, "FizzBuzz", result)
    result = np.where(mod3 & ~mod5, "Fizz", result)
    result = np.where(mod5 & ~mod3, "Buzz", result)

    return result

print(FizzBuzz(61, 75))