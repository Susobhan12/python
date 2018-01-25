Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[1,2,3,4,5,6,7,8,9]
>>> list[:8]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list[1:_]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list[1:_]
TypeError: slice indices must be integers or None or have an __index__ method
>>> list[-1]
9
>>> list[2:2:1]
[]
>>> list[1: ]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> list[1:2:1]
[2]
>>> 
