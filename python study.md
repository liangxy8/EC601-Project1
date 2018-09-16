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
words=['defenestrate', 'cat', 'window', 'defenestrate'] 
```   

- for else  
在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出.   

- range()  
创建一个整数列表
```python
range(start, stop[, step]) (start 0, step 1)  
r[i] = start + step*i,  i >= 0 and r[i] < stop.
```
- break,continue  
continue跳过当前循环的剩余语句，然后继续进行下一轮循环，而break跳出整个循环  
- 


- str()
返回给定的内容  [tutorial](https://www.programiz.com/python-programming/methods/built-in/str)
```python
str('object', encoding='utf-8', errors='strict')
```  
