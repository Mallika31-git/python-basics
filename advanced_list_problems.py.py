#1 seperating numbers
a=[1,2,-1,3,4,-3,-6,0,5]
x=[]
y=[]
z=[]
for i in a:
    if i>0:
        x.append(i)
    elif i==0:
        y.append(i)
    else:
        z.append(i)
print("positive numbers list:",x)
print("zeros containing in the list",y)
print("negative numbers list:",z)

#2 ascending and descending
a=[9,8,7,6,5,4,1]
ascending=True
descending= True
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        ascending=False
    elif a[i]<a[i+1]:
         descending=False
if   ascending:      
    print("the list is sorted and in ascending order")
elif    descending:
    print("the list is sorted and in descending order")
else:
    print("the list is not sorted")
            
 

#3 missing number
l=[1,2,3,5,7,9]
for i in range(len(l)-1):
    if l[i]+1 not in l:
        print("missing number",l[i]+1)
        
#4 largest, 2nd largest,3rd largest
n=int(input("enter the range:"))
l=[]
largest=largest_2=largest_3=float('-inf')
for i in range(n):
    x=int(input(f"enetr no.{i+1}:"))
    if x>largest:
        largest_3=largest_2
        largest_2=largest
        largest=x
     
    elif x>largest_2 and x!=largest:
        largest_2=x
    elif x>largest_3 and x!=largest_2 and x!=largest:
        largest_3=x
print("largest number:",largest)
print("2nd largest  number:",largest_2)
print("3rd largest number:",largest_3)

#5 finding pairs whose sum is 10
nums=[1,9,2,8,3,7,4,6]
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==10  :
            print(f"{nums[i],nums[j]}")
            
#6 moving zeroes to end
l=[1,2,0,8,0,6]
m=[]
n=[]
for i in l:
    if i==0:
        m.append(i)
    else:
        n.append(i)
result=n+m
print(result)