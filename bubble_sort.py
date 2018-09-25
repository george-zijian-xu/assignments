list1=[1,55,3,6,3,664,6,3,6,4,754,85,268,785,78,34,7,3,8,5,434,77,37,19,69,28,45]
index = 0
switched = True 
#while (switched == True):
#	index = 0
#	switched = False
while (index<len(list1)-1):
	if (list1[index]>list1[index+1]):
		list1[index],list1[index+1]=list1[index+1],list1[index]
		switched = True
	index = index+1

print(list1)
       
