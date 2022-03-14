


# File Handling
# File Handling


'''
f = open('text.txt','w')
f.write('hello world')
f.close()
'''

'''
f = open("text.txt", "r")

print(f.read())


f = open("text.txt", "r")

print(f.read(15))
'''
'''
f = open("text.txt", "r")

print(f.readline())
print(f.readline())
'''
'''
f = open("text.txt", "r")
for x in f:
    print(x)
'''


'''
f = open('text.txt','a')
f.write(' hello world, I am good to see you')
f.close()

'''
'''

f = open('text.txt', 'r')
print(f.read())

'''



# Numpy
# Numpy
'''
import numpy as np

print(np.__version__)
'''

#import numpy
'''
import numpy
a = numpy.array([3,6,9])
print(a/3)
'''
'''
import numpy as np
a = np.array([1,2,3,4])
print(a/1)
print(type(a))
'''

# 0 - D
'''
import numpy as np

a = np.array(500)

print(a)
'''

'''

import numpy as np

a = np.array(42)

print(a)
'''

# 1-D
'''
import numpy as np
b = np.array([1,2,3])
print(b)
'''
# 2-D
'''
import numpy as np
c = np.array([[1,2,3],[4,5,6]])
print(c)
'''
#3-D
'''
import numpy as np
d = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]] )
print(d)

'''

# check for dimention
'''
import numpy as np

a = np.array(50)
b = np.array([1,2,3,4,5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


`print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
'''

#array indexing
'''
import numpy as np
h = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(h[1,1,1])
'''

'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:6])
'''



# SciPy
# SciPY


'''
import scipy

print(scipy.__version__)

'''



''' 
from scipy import constants

print(constants.minute)


from scipy import constants

print(constants.kilo)

from scipy import constants

print(constants.kibi)

from scipy import constants

print(constants.grain)


from scipy import constants

print(constants.arcsec)


from scipy import constants

print(constants.week)

from scipy import constants

print(constants.bar)
'''

import matplotlib

print(matplotlib.__version__)



















