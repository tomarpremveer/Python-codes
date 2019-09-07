
def hextodec(st):
    dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    i=len(st)-1
    decn=0
    count=0
    while i>=0:
        decn+=dic[st[i]]*(16**count)
        count+=1
        i=i-1
    return decn
if __name__=="__main__":
    st=str(input())
    print(hextodec(st))
