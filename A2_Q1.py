def compute_Dist(lis,pnt):
    import math
    ans=[]
    temp = []
    for i in range(0,len(lis)):
        x,y = lis[i]
        dist = math.sqrt((pnt[0]-x)**2 + (pnt[1]-y)**2)
        temp.append((i,dist))
    temp.sort(key = lambda x:x[1])
    for i in range(0,len(temp)):
        ans.append(lis[temp[i][0]])
    return ans[0:5]

pnt = (0,0)
lis = [(5,5),(1,1),(2,2),(3,3),(4,4),(6,6)]
print(compute_Dist(lis,pnt))