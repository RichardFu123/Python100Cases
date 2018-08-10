#list  
#新建列表  
testList=[10086,'中国移动',[1,2,4,5]]  
  
#访问列表长度  
print (len(testList)  )
#到列表结尾  
print (testList[1:])
#向列表添加元素  
testList.append('i\'m new here!')  
  
print (len(testList)  )
print (testList[-1]  )
#弹出列表的最后一个元素  
print (testList.pop(1)  )
print (len(testList)  )
print (testList  )
#list comprehension  
#后面有介绍，暂时掠过  
matrix = [[1, 2, 3],  
[4, 5, 6],  
[7, 8, 9]]  
print (matrix  )
print (matrix[1]  )
col2 = [row[1] for row in matrix]#get a  column from a matrix  
print (col2  )
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item  
print (col2even)
