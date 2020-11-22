def waitingTime(processes,n,bt,wt):
	
def turnAroundTime(processes,n,bt,wt,tat):
    for i in range(n): 
        tat[i]= bt[i]+wt[i]

def averageTime(processes, n, bt):
    wt = [0] * n 
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    waitingTime(processes, n, bt, wt)

    turnAroundTime(processes,n,bt,wt,tat)
    
    print("processes"+ '\t'+"burstTime"+'\t'+"waitingTime"+'\t'+"turnAroundTime")

    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        
        print(" " + str(processes[i]) + "\t\t" + str(bt[i]) +"\t\t"+ str(wt[i]) + "\t\t" + str(tat[i]))

    print("Average waiting time = ",(total_wt /n)) 
    print("Average turn around time = ", total_tat / n)     
       
if __name__ =="__main__":

    n=int(input("No. of processes do you want?"))
    
    processes=[]
    for i in range(1,n+1):
         processes.append(i)
     
    burstTime=[] 
    for i in range(1,n+1):
    
         a=int(input("burstTime for {} process ".format(i)))
         burstTime.append(a)
    


    averageTime(processes,n,burstTime)
	    	