#ALPHA BETA PRUNING
list1=[-1,3,5,1,-6,-4,0,9]
MIN=-10000
MAX=+10000
def minimax(depth,flag,nodeindex,alpha,beta):
    if (depth==3):
        return list1[nodeindex];
    if (flag):
        maxeval=MIN
        for i in range(2):
            eval=minimax(depth+1,False,nodeindex*2+i,alpha,beta)
            maxeval=max(maxeval,eval)
            alpha=max(alpha,eval)
            if (alpha>=beta):
                break
        return maxeval
    else:
        mineval=MAX
        for i in range(2):
            eval=minimax(depth+1,True,nodeindex*2+i,alpha,beta)
            mineval=min(mineval,eval)
            beta=min(beta,eval)
            if (alpha>=beta):
                break
        return mineval
print(minimax(0,True,0,MIN,MAX))
