#enter 2 numbers eg 15 7
#then enter json line by line(press enter after each line) based on 1st number(15 lines in this case)
#then the next 7 names of variablespress enter after each line)(as in this eg)

def parsing():
    a,b=map(int,raw_input().split())
    n=[]
    m=[]
    s=''
    for i in range(a):
        inp=raw_input()
        
        n.append(inp)
    for i in range(b):
        inp=raw_input()
        
        m.append(inp)

    for i in range(0,b):
        if m[i].find('.')!=-1:
            fin=m[i].find('.')
            m[i]=m[i][fin+1:]
        
    for i in range(0,len(m)):
        x=m[i]
        flag=False
        answer=''
        for j in range(0,len(n)):
            y=n[j]
            if x in y:
                flag=True
                co=n[j].find(':')
                if n[j].find(',')!=-1:
                    com=n[j].find(',')
                else:
                    com=n[j].find('}')
                answer=n[j][co+1:com]
                
                answer=answer.strip()
            if answer=='nul':
                answer='null'
                
                
            if flag==False:
                answer='null'
        print answer
          
parsing()


