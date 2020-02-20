# Markhus Dammar
# 2/20/2020
# This is the driver for the linked list

import time
from NodeClass import ListNode
from NodeClass import LinkedList

myList = LinkedList()
print("Here's the empty list")
print(myList)
time.sleep(2)
print("Now, let's add to it.")
myList.prepend(30)
print(myList)
time.sleep(0.7)
myList.prepend("255")
print(myList)
time.sleep(0.7)
myList.prepend('Hello World')
print(myList)
time.sleep(0.7)
myList.prepend(6)
print(myList)
time.sleep(0.7)



