list_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_0.reverse()           
print(list_0)
list_0 = [str (x) for x in list_0]  
str_0 = ''.join(list_0)
print(str_0)
str_1 = str_0[3:9]
str_2 = str_1[::-1]   
print(str_2)
int_0 = int(str_2)
print("转换为二进制：",bin(int_0))
print("转换为八进制：",oct(int_0))
print("转换为十六进制：",hex(int_0))