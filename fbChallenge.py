#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:54:04 2019

@author: rajeshnarayanarao
"""

def helper_dp(data, k, memo):
    if k == 0:
        return 1
    s = data.length - k
    if data[s] == '0':
        return 0
    if memo[k] != None:
        return memo[k]
    result = helper_dp(data, k - 1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper_dp(data, k-2, memo)
    memo[k] = result
    return result

def num_ways_dp(data):
    memo = [None] * (data.length + 1) #initialize to null's
    return helper_dp(data, data.length, memo)