import numpy as np
import matplotlib.pyplot as plt

from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits

x=np.linspace(0,2*np.pi,1000)
y=np.sin(x)

data = Table([x,y],names=['x','sin(x)'])
ascii.write(data,'table.txt',format='commented_header')
data_in=ascii.read('table.txt')
print(data_in)