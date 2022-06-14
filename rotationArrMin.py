def search_min(arr,length):
    if arr==None or length<=0:
        raise Index("value not exist")
    index1=0
    index2=length-1
    mid=0
    while arr[index1]>=arr[index2]:
        if index2-index1==1:
            mid=index2
            break
        mid=(index1+index2)//2
        if arr[mid]>=arr[index1]:
            index1=mid
        elif arr[mid]<=arr[index2]:
            index2=mid
    return arr[mid]

"""
针对存在index1、index2、与mid相等的情况时，需要采用
顺序查找的方法进行检索。
"""



arr=[3,4,5,1,2]
a=search_min(arr,5)
print(a)

