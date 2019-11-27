#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment 03 | Task01: Make a calculator using Python with addition , subtraction , multiplication , division and power.

print("------------------CALCULATOR-----------------")
option=input("Select Any Operation\n 1:Addition\n 2:Multiplication\n 3:Division\n 4:power\n")

if option=="1":
    num1=int(input("Enter Num1:"))
    num2=int(input("Enter Num2:"))
    print("Sum is:",num1+num2)

elif option=="2":
    num1=int(input("Enter Num1:"))
    num2=int(input("Enter Num2:"))
    print("Product is:",num1*num2)

elif option=="3":
    num1=int(input("Enter Num1:"))
    num2=int(input("Enter Num2:"))
    print("division is:",num1/num2)

elif option=="4":
    base=int(input("Enter Base"))
    power=int(input("Enter Power"))
    print("Result:",base**power)


# In[3]:


# Assignment 03 | Task02: 

mylist=['1','orange','2','3','4','apple']
mynewlist = [s for s in mylist if s.isdigit()]

for i in range(0,len(mynewlist)):
    print(mynewlist[i])


# In[4]:


# Assignment 03 | Task03: 
dictionary = {0:25, 1:28, 2:100, 3:500}
print("Before Adding Key:",dictionary)
dictionary.update({4:30})
print("After Adding key:",dictionary)


# In[5]:


# Assignment 03 | Task04: 
dictionary = {0:25, 1:28, 2:100, 3:500}
SumCount=0

for i in range(0,len(dictionary)):
    SumCount=SumCount+dictionary[i]
    
print("Sum of dictionary values is:",SumCount)


# In[6]:



# Assignment 03 | Task05: 

list1 = [10,8,7,5,3,2,1,44,2,55,55,88,22,55] 
size = len(list1) 
repeated = [] 
for i in range(size): 
        k = i + 1
        for j in range(k,size): 
            if list1[i] == list1[j] and list1[i] not in repeated: 
                repeated.append(list1[i]) 
print("Repeated values in list are:",repeated) 
  


# In[8]:


# Assignment 03 | Task06: 

dictionary = {0:25, 1:28, 2:100, 3:500}
key=int(input("Enter Any key Value to check:"))

if key in dictionary:
    print("This key is present in dictionary")
else:
    print("Not Present")


# In[ ]:




