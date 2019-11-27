#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Arun Kumar Assignment 1 
#Task1:Print the poem

print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t      Up above the world so high,")
print("\t      Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")


# In[27]:


#Arun Kumar asssignment1 
#Task02: Write a Python program to get the Python version you are using

import sys

print("your current python version is:",sys.version)


# In[32]:


# Arun Kumar Asssignment 1
#Task3: Display Current Date and time

from datetime import date 
from datetime import datetime

getdate = date.today()
now = datetime.now()
getTime = now.strftime("%H:%M:%S")

print("Current Date is:",getdate)
print("Current Time is:",getTime)





# In[33]:


#Arun Kumar asssignment1 
#Task04: Calculate area of circle by taking radius as input.

pie=22/7
radius=float(input("Enter Radius of Circle:"))
Area=pie*((radius*radius))
print("Area of circle is:",Area)


# In[26]:


#Arun Kumar asssignment1 
#Task05: Write a Python program which accepts the user's first and last name 
#and print them in reverse order with a space between them.

firstName=input("Enter your First Name:")
lastName=input("Enter your last Name:")


print("\nBefore Reverse:")
print(firstName,"",lastName)

print("\nAfter Reverse:")
print(firstName[::-1]," ",lastName[::-1])


# In[30]:


#Arun Kumar asssignment1 
#Task06: Write a python program which takes two inputs from user and print them addition

input1=int(input("Enter Input1:"))
input2=int(input("Enter Input2:"))
print("Addition is:",input1+input2)



# In[ ]:





# In[ ]:




