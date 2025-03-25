n=int(input())
arr=[]
arr2=[]
rem=0
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    if(arr[i]%2==1):
        rem=arr[i]%10
        arr2.append(arr[i]*rem)
    else:
        temp=arr[i]//10
        rem=temp%10
        arr2.append(arr[i]*rem)    
sum=0
for i in range(len(arr2)):
    sum+=arr2[i]
print(sum)