import sys
import zlib

a = "this string needs compressing"

text=b"""This function is the primary interface to this module along with 
decompress() function. This function returns byte object by compressing the data 
given to it as parameter. The function has another parameter called level which 
controls the extent of compression. It an integer between 0 to 9. Lowest value 0 
stands for no compression and 9 stands for best compression. Higher the level of 
compression, greater the length of compressed byte object."""
a_result = zlib.compress(a.encode())

b_result = zlib.compress(text)
print(sys.getsizeof(a_result))
print(sys.getsizeof(b_result))
# print(zlib.decompress(a).decode())