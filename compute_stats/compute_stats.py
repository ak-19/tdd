from math import sqrt

def read_ints(file_path):
    data = []
    with open(file_path,  'r') as f:
        for line in f:
            data.append(int(line))
    return data

def count(data):
    return len(data)

def summation(data):
    return sum(data)

def average(data):
    return summation(data) / count(data)

def minimum(data):
    return min(data)

def maximum(data):
    return max(data)    

def harmonic_mean(data):
    divided = count(data)
    divided_by = sum(map(lambda x: 1/x, data))
    return divided / divided_by

def variance(data):
    mean = average(data)
    sum_square_deviation = sum([(x - mean)**2 for x in data])
    return sum_square_deviation / count(data)

def standard_dev(data):
    return sqrt(variance(data))