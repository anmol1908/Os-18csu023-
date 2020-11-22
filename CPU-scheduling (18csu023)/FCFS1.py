def waitingTime(processes,n,bt,wt,at):
     
    time = [0] * n  
    time[0] = 0
    wt[0] = 0
  
    for i in range(1, n):  
          
    
        time[i] = (time[i - 1] + bt[i - 1]) 
        wt[i] = time[i] - at[i]  
  
        
        if (wt[i] < 0): 
            wt[i] = 0

def turnAroundTime(processes,n,bt,wt,tat):
    for i in range(n): 
        tat[i]= bt[i]+wt[i]

def averageTime(processes, n, bt, at):
    wt = [0] * n 
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    waitingTime(processes, n, bt, wt,at)

    turnAroundTime(processes,n,bt,wt,tat)
    
    print("processes"+ '\t'+"burstTime"+'\t'+"arrivalTime"+'\t'+"waitingTime"+'\t'+"turnAroundTime")

    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        
        print(" " + str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t " +str(at[i])+"\t\t"+ str(wt[i]) + "\t\t" + str(tat[i]))

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
    
    arrivalTime=[] 
    for i in range(1,n+1):
         b=int(input("arrivalTime for {} process ".format(i))) 
         arrivalTime.append(b) 

    averageTime(processes,n,burstTime,arrivalTime)