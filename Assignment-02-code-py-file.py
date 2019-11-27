#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assignment 02 | Task01: Write a program which takes 5 inputs from user for different subject’s
#marks, total it and generate mark sheet using grades 
print("-----------------Enter Marks For 5 Subjects out of 100------------------------")
sub1=int(input("English:"))
sub2=int(input("Maths:"))
sub3=int(input("Urdu:"))
sub4=int(input("Science:"))
sub5=int(input("Social Studies:"))
obtained=sub1+sub2+sub3+sub4+sub5
Grade=""
percent=int((obtained/5)*1)
if percent>=90 and percent<=100:
    Grade="A"
    
elif percent>=80 and percent<=89:
    Grade="B+"
    
elif percent>=70 and percent<=87:
    Grade="B"
    
elif percent>=60 and percent<=69:
    Grade="C"

elif percent>=50 and percent<=59:
    Grade="D"

elif percent<50:
    Grade="F"

    
print("\n-----Marksheet-----")
print("Grade",Grade," ",percent,"%","obtained Marks:",obtained)


# In[2]:


# Assignment 02 | Task02: Write a program which take input from user and identify that the given number is even or odd?

num=int(input("Enter Any Integer to check if it is even/odd?"))

if num%2==0:
    print("Number:",num,"is even")
else:
    print("Number:",num,"is odd")


# In[3]:


# Assignment 02 | Task03: Write a program which print the length of the list?

lis=[1,2,3,4,5,6]
print("Length of this list is:",len(lis))


# In[4]:


# Assignment 02 | Task04: Write a Python program to sum all the numeric items in a list?

mylist=[1,2,3,4,5,6,7,8,9]
count=0
#we can do it by using sum function
print("Sum of list values using sum function is:",sum(mylist))

#or another way is to use for loop for sum
for i in range(0,len(mylist)):
    count=count+mylist[i]

print("Sum of list values using for loop is:",count)


# In[5]:


# Assignment 02 | Task05: Write a Python program to get the largest number from a numeric list.


mylist=[22,55,66,1,88,90]
print("Max Value in this list is:",max(mylist))



# In[6]:


# Assignment 02 | Task06: write a program that prints out all the elements of the list that are less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print("Values that are less than 5")

for i in range(0,len(a)):
    if a[i]<5:
        print("Value",i+1,":",a[i])


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




