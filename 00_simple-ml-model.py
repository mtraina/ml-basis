#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
example took from https://towardsdatascience.com/simple-machine-learning-model-in-python-in-5-lines-of-code-fe03d72e78c6
'''

'''
prepare the data
'''
from random import randint

TRAIN_SET_LIMIT = 10000
TRAIN_SET_COUNT = 4

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()

for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + 2*b + 3*c
    TRAIN_INPUT.append([a,b,c])
    TRAIN_OUTPUT.append(op)
    
'''
create and train the model
'''
from sklearn.linear_model import LinearRegression

predictor = LinearRegression()
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

'''
test the model
'''
X_TEST = [[10,20,30]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome: {}\nCoefficients:{}'.format(outcome, coefficients))