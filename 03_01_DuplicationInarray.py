

class Duplocation:

    def radix_find_dup(self,array):
        h=[0 for _ in range(len(array))]
        for x in array:
            h[x]+=1
        dup=[]
        for i in range(len(array)):
            if h[i]>1:
                dup.append(i)
        return dup


    def DuplicationInarray(self,array):
        #判断数组是否为空
        if  len(array)<1:
            return False

        #判断数组是否越界
        for i in range(len(array)):
                if array[i]<0 or array[i]>len(array)-1:
                    return False

        dp=[]#记录重复值的空数组
        for i in range(len(array)):
            while array[i]!=i:
                if array[i]==array[array[i]]:
                    dp.append(array[i])     #找到重复值之后，就不需要后续的交换步骤，所以要跳出while循环
                    break
                #当不满足的时候需要交换两值
                #第一种写法：
                # arr=array[i]
                # array[i]=array[array[i]]
                # array[arr]=arr
                #第二种写法：
                arr=array[i]
                array[i],array[arr]=array[arr],array[i]
        return dp


    #用于解决查找只有一个重复值或者任意重复值的形式
    def binary_search_dup(self,array):
        if  len(array)<1:
            return False
        start=1
        end=len(array)-1
        while end>=start:
            mid=(end-start)//2+start
            count=self.countRange(array,start,mid)
            if end==start:
                if count>1:
                    return start
                else:
                    break
            if count>(mid-start+1):
                end=mid
            else:
                start=mid+1
        return -1


    def countRange(self,array,start,end):
        count=0
        for i in range(len(array)):
            if array[i]>=start and array[i]<=end:
                count+=1
        return count

find=Duplocation()
array=[2,3,5,4,3,2,6,7]
a=find.DuplicationInarray(array)
print(a)
b=find.radix_find_dup(array)
print(b)
c=find.binary_search_dup(array)
print(c)