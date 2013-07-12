# bilibili comments counting 
# input file: bilibili popup comments .ass file
# function: counting the number of comments per second and show it visually by ASCII Art
import re

def wtl(line):# regular expression
    words=re.findall(r'Dialogue+.+',line)
    if len(words)>0:
        words=re.findall(r'[0-9]:[0-9]{2}:[0-9]{2}',words[0])# matching time
    return words



def srt(d,flag=0,r=False):#sort
    return sorted(d.iteritems(), key=lambda x: x[flag] , reverse=r)

k=999
dic={}
fname='1.ass'  # input file
fr=file(fname,'r')
while True or k>0:  # test switch :  or-and
    line=fr.readline()# read in 
    li=wtl(line)
    if len(li)>0:
        tp=li[0]  # tp is a time point
        #print ky
        if dic.has_key(tp) is False:  #count
            dic[li[0]]=1
        else:
            dic[li[0]]+=1
    if len(line)==0:
        break
    k-=1

fr.close()

lst=srt(dic,0)
cnt=0 #comments counter
out_f = open(fname+'.out',"wb")
for e in lst:                        #output
    print >>out_f,e[0],'=',e[1],' ',
    if e[1]<10:
        print >>out_f,'',
    p=0
    while p<e[1]:
        print >>out_f,'#',
        p+=1
    print >>out_f,''
    cnt=cnt+int(e[1])  #counting
    
out_f.close()
print fname,cnt

