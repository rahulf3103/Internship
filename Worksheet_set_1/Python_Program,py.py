#!/usr/bin/env python
# coding: utf-8

# In[1]:


"Factorial of a number"

i=int(input("enter number"))
fac=1
while (i>0):
    fac = fac*i
    i=i-1
print("Factorial = ",fac)


# In[5]:


"Write a python program to find whether a number is prime or composite."

num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# In[6]:


"write a python program to check whether a given string is palindrome or not"

def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")


# In[7]:


"Write a Python program to get the third side of right-angled triangle from two given sides."

import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# In[8]:


"Write a python program to print the frequency of each of the characters present in a given string."

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


# In[ ]:




