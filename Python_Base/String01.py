import time
import datetime

strS1 = 'Hello'
strS2 = "-World"
strS3 = strS1+strS2
print('ld' in strS1+strS2)

print(strS2[5])

for x in strS2:
    print(x)

# for s in strS1+strS2: print(s) duyệt qua chuỗi rất đơn giản

# strS3 = "%s %s %d"  % (strS1, strS2, 100)
# strS3 = strS2[0:3]
# strS3 = strS2[-5]
# strS3 = strS2.replace('-',"+++++").replace('l','L')
# strS3 = 'HH'+strS2[3:]
strS4 = [strS1, strS2, strS3, 0, 1, 5, 9, 7, 5, 12, 15, "5", {'a': 30}, '20']
# print(99 in strS4)
# print(type(strS4[-1]['a']))
# strS5 = strS4.count(5)
# strS5 = type(strS4[4])
strS4.insert(4, "Thêm giá trị vào Vị trí 4")
# strS4.pop(4) # bỏ đi phần tử tại vị trí 4
strS4.remove("5")  # bỏ đi phần tử có giá trị 5
# strS5 = strS4.sort(reversed=True) List có cả giá trị số và string thì ko thể sort
# strS5  = len(strS4)
strS5 = strS4.clear()
# strS5 =strS4.sort()
# print(strS5)
# ----------------------------------------------------Dict---------------------
# dic1={}
# dic1['a']='alpha'
# dic1['b']='gama'
# dic1['c'] = [strS1, strS2, strS3, 0, 1, 5, 9, 7, 5, 12, 15, "5"]
# dic1[0]="Chào các cụ"
# #dic1['d']={'o':'Omega'}
# # print(dic1)
# # print(len(dic1))
# #del dic1[0] # Xóa phần tử ke là 0
#
# # print(len(dic1.keys()))
# #for key in dic1: print(dic1[key])
# # print(list(dic1.values()))
# # print(list(dic1.items()))
# print('15' in dic1)
strS6Set = {1, 5, 6, 3, 1, 3, 8, 9}
strS7Tuple = (0, 1, 5, 9, 7, 5, 12, 15, "5", {'a': 30})
# $strS7Tuple =
# print(type(strS7Tuple))

# print('s.dfsdfs.dfsd.fsd'.split('.'))
# print(4 % 2)

# trong list numbers muốn tìm số nguyên tố hoặc chính phương?thì làm cánh nào?
strS8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
         59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, \
         86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, ]
# print(id(strS8))
# strSoNguyenTo=[]
#
# for x in strS8:
#     if x>2:
#         for i in range(2,x):
#            print(strSoNguyenTo.append(x))
i = 0
x = 5

# for x in strS8:
# def nSum_Tong(x=0,y=0):
#     pass
#
# print (nSum_Tong(3,9))


# Function definition is here
# def changeme(mylist):
#     "This changes a passed list into this function"
#     try:
#         mylist = [1, 2, 3, 4]  # This would assi new reference in mylist
#         print("Values inside the function: ", mylist)
#         return
#     except ValueError:
#         print('lỗi mịa nó rùi')


# Now you can call changeme function
# mylist = [10, 20, 30]
# changeme(mylist)
# print("Values outside the function: ", mylist)
#
# def fnTest(b):
#     d = {'a': 'Alpha'}
#     b= {'k' : "Hieu bui thanh"}
#     try:
#         print(d['b'])
#     except KeyError:
#         print('Lỗi mịa nó rùi')
#
# fnTest('b')
# fnTest('b')

# import Hieubt_Module  as MyModule
# from Hieubt_package.Hieubt_Module import Hieubt_func
#
# Ngaysinh = MyModule.Hieubt_func()
# Ngaysinh1  = Hieubt_func()
# print(Ngaysinh + '/' +  Ngaysinh1)

# items = [1, 2, 3, 4, 5]
# squared = []
#
# # squared = list(map(lambda x: x**2, items))
# for i in items:
#     squared.append(i ** 2)
#
# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
#
# print(squared[4])