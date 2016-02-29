def coder():

 message=input("Please enter Your message:")
 length=len(message)   
 d=list(message)  
 e=[0]*int(length)
 f=[0]*int(length)
 g=[0]*int(length)

 for j in range (0,int(length)):   
    e[j]=ord(d[j])

 for k in range (0,int(length)):   
    f[k]=e[k]+4

 for l in range (0,int(length)):   
    g[l]=chr(f[l])    
 cmess=""
 for m in range (0,int(length)):   
    cmess+=(str(g[m])) 
    
 print "Your message is "+message
 print "The coded message is "+ cmess

 return cmess

coder()



