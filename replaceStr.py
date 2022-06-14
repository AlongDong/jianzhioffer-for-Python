class Replacblank:



    def countStr(self,string):
        count=0
        strarr=[]
        for s in string:
            strarr.append(s)
            if s==" ":
                count+=1
        for j in range(2*count):
            strarr.append(" ")
        return strarr

    def replaceStr(self,string):
        originallength=len(string)-1
        newstr=self.countStr(string)
        newlength=len(newstr)-1
        while (originallength>=0 and newlength>originallength):
            if newstr[originallength]==" ":
                originallength-=1
                newstr[newlength]="0"
                newlength-=1
                newstr[newlength]="2"
                newlength-=1
                newstr[newlength]="%"
                newlength-=1
            else:
                newstr[newlength]=newstr[originallength]
                newstr[originallength]=" "
                newlength-=1
                originallength-=1
        send=str()
        for s in newstr:
            send+=s

        return send
        
    # def replaceStr(self,string):
    #     newstr=str()
    #     for i in string:
    #         if i==" ":
    #             newstr+="%"
    #             newstr+="2"
    #             newstr+="0"   
    #         else:
    #             newstr+=i

    #     return newstr     

string="i am dongalong thank you"
a=Replacblank()
b=a.replaceStr(string)
print(b)


