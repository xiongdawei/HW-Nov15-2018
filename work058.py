#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:13:04 2018

@author: davidxiong
"""



class Stack():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def get(self):
        return self.items
    
    def reverse_stack(self):
       
        listt=[]
        while len(self.items)>0:
            listt.append(self.items[-1])
            self.items.remove(self.items[-1])
        return listt
    
    def parChecker(self,string):
        string = list(string)
        index = 0
        n = 0
        j = 0
        while index<len(string):
           
            if string[index] == "(":
                n+=1
            elif string[index] == ")":
                j+=1
            index +=1
        if n==j:
            return True
        else:
            return False
 
    def convert_binaray(self,number):
        s = Stack()
        while number>0:
            s.push(number%2)
            number = number//2
        return s.get()
    
    def convert_everything(self,number,system):
        index = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
        s = Stack()
        while number >0:
            s.push(index[number%system+1])
            number = number//system
        return s.get()
    
    def every_system(system1,number1,system2,number2):
        index = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
        s = Stack()
        number1 = list(number1)
        for i in number1:
            number[i] = number[i]*system1**(len(number1)-1)
        
        
        
        
        
        
        
            
        
        
            
        
                     
          
s = Stack()

#print(s.isEmpty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.isEmpty())
#s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())
#print(s.get())
#s.push(5)
#print(s.isEmpty())
#print(s.get())
#print(s.reverse_stack())
#abc = "()"
#print(s.parChecker(abc))
#print(s.diff_parChecker(abc))
print(s.convert_binaray(89))
print(s.convert_everything(452,16))



    
    
        
