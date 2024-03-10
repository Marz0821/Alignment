import pickle
import numpy as np
import matplotlib.pyplot as plt

def FindNNMean (data):
 j=0
 NNM=np.zeros((81))
 AlArr=np.zeros((51))
 for g in range (0,4001):
  m=g-j
  AlArr[m]=data[g]
  if g%50==0:
   h=g//50
   NNM[h]=np.mean(AlArr)
   j=g

 return NNM


tna=np.array ([[0,1,2,3],[0,1,2,4],[0,1,3,4],[0,2,3,4],[1,2,3,4]])
gen=np.zeros((81))
NNMCalc=np.zeros((81,24))


for i in range(0,4001,50):
 j=i//50
 gen[j]=i

tna=np.array ([[0,1,2,3],[0,1,2,4],[0,1,3,4],[0,2,3,4],[1,2,3,4]])

for team_idx in range (0,5):
        agent_idx1= tna[team_idx,0]
        agent_idx2= tna[team_idx,1]
        agent_idx3= tna[team_idx,2]
        agent_idx4= tna[team_idx,3]

        filepath = r"SS/"+str(team_idx)+"-"+str(agent_idx1)+'.pkl'
        file=open(filepath, 'rb')
        data1=pickle.load(file)
        file.close
        idx=0+(team_idx*4)
        NNMCalc[:,idx]=FindNNMean (data1)


        filepath = r"SS/"+str(team_idx)+"-"+str(agent_idx2)+'.pkl'
        file=open(filepath, 'rb')
        data2=pickle.load(file)
        file.close
        idx=1+(team_idx*4)
        NNMCalc[:,idx]=FindNNMean (data2)

        filepath = r"SS/"+str(team_idx)+"-"+str(agent_idx3)+'.pkl'
        file=open(filepath, 'rb')
        data3=pickle.load(file)
        file.close
        idx=2+(team_idx*4)
        NNMCalc[:,idx]=FindNNMean (data3)

        filepath = r"SS/"+str(team_idx)+"-"+str(agent_idx4)+'.pkl'
        file=open(filepath, 'rb')
        data4=pickle.load(file)
        file.close
        idx=3+(team_idx*4)
        NNMCalc[:,idx]=FindNNMean (data4)

plt.plot(gen, NNMCalc[:,0], color='purple', label = 'Agent 0')
plt.plot(gen, NNMCalc[:,1], color='green', label = 'Agent 1')
plt.plot(gen, NNMCalc[:,2], color='red', label = 'Agent 2')
plt.plot(gen, NNMCalc[:,3], color='blue', label = 'Agent 3')
plt.ylim([0,100])
plt.xlim([0,4000])        
plt.legend(loc='lower right')
plt.xlabel("Generation")
plt.ylabel("Percent Alignment")
plt.title("Percent Alignment for Team 0")

#plt.plot(gen, NNMCalc[:,4], color='purple', label = 'Agent 0')
#plt.plot(gen, NNMCalc[:,5], color='green', label = 'Agent 1')
#plt.plot(gen, NNMCalc[:,6], color='red', label = 'Agent 2')
#plt.plot(gen, NNMCalc[:,7], color='orange', label = 'Agent 4')
#plt.ylim([0,100])
#plt.xlim([0,4000])        
#plt.legend(loc='lower right')
#plt.xlabel("Generation")
#plt.ylabel("Percent Alignment")
#plt.title("Percent Alignment for Team 1")

#plt.plot(gen, NNMCalc[:,8], color='purple', label = 'Agent 0')
#plt.plot(gen, NNMCalc[:,9], color='green', label = 'Agent 1')
#plt.plot(gen, NNMCalc[:,10], color='blue', label = 'Agent 3')
#plt.plot(gen, NNMCalc[:,11], color='orange', label = 'Agent 4')
#plt.ylim([0,100])
#plt.xlim([0,4000])        
#plt.legend(loc='lower right')
#plt.xlabel("Generation")
#plt.ylabel("Percent Alignment")
#plt.title("Percent Alignment for Team 2")

#plt.plot(gen, NNMCalc[:,12], color='purple', label = 'Agent 0')
#plt.plot(gen, NNMCalc[:,13], color='red', label = 'Agent 2')
#plt.plot(gen, NNMCalc[:,14], color='blue', label = 'Agent 3')
#plt.plot(gen, NNMCalc[:,15], color='orange', label = 'Agent 4')
#plt.ylim([0,100])
#plt.xlim([0,4000])        
#plt.legend(loc='lower right')
#plt.xlabel("Generation")
#plt.ylabel("Percent Alignment")
#plt.title("Percent Alignment for Team 3")

#plt.plot(gen, NNMCalc[:,16], color='green', label = 'Agent 1')
#plt.plot(gen, NNMCalc[:,17], color='red', label = 'Agent 2')
#plt.plot(gen, NNMCalc[:,18], color='blue', label = 'Agent 3')
#plt.plot(gen, NNMCalc[:,19], color='orange', label = 'Agent 4')
#plt.ylim([0,100])
#plt.xlim([0,4000])        
#plt.legend(loc='lower right')
#plt.xlabel("Generation")
#plt.ylabel("Percent Alignment")
#plt.title("Percent Alignment for Team 4")    


plt.show()