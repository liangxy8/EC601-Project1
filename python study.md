# 1. Python Basic
1. __+, -, *, /__
2. do floor division and get an integer result：__//__  
     calculate the remainder：__%__  
     calculate the power: __**__
3. string:both single and double quotes:&nbsp;__'', ""__  
   string can be concatenated by using__*, +__. exp:3*'un'+'ium'is'unununium'
   string can't be changed, if need a different, should create a new one  
   length of a string: __len()__  
4. lists can be changed and concatenation  
   add neew items at the end of the list: __.append()__  
5. __end__ can be used to avoid the newline after the output. exp: __print(a, end=',')__  

# 2. Control Flow Tools  
- while 
```python
while condition：
      balabalabala
```
- if
```python
if condition1:
   balaba
elif condition2:
   balabala
else:
    balabala
```  
- for  
```python
words = ['cat', 'window', 'defenestrate']
for w in words[:]:
     if len(w) > 6:
         words.insert(0, w)
```  
words=['defenestrate', 'cat', 'window', 'defenestrate']
