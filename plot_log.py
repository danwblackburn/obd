import matplotlib.pyplot as plt 

import numpy as np

import sys
import csv


if(len(sys.argv) > 1):
    print(sys.argv[1])
    file = open(sys.argv[1])
    reader = csv.reader(file, delimiter=',')
    headers = next(reader)
    file.close

    data = np.genfromtxt(sys.argv[1], delimiter=",", dtype=float, skip_header=1)

    time = data[:, 0]
    reading = data[:, 1]
    plt.plot(time, reading)
    plt.show()
else:
    print('No file given')
            
    
