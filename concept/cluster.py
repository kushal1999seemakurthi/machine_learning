class K_means:

  def random_initialization(self,x,k,p=0):
    m,n=x.shape
    rc=np.random.choice(m,k)
    v=[x[i] for i in rc]
    vv=np.array(v)
    if p==1:
      print("\n","_______intialization of means______","\n",v)
      plt.figure()        
      plt.plot(x[:,0],x[:,1],".")  
      plt.plot(vv[:,0],vv[:,1],"X")
      plt.show()
    return vv

  def dist(self,x,y):
    a=x
    b=y
    return np.linalg.norm(a-b)

  def cluster(self,clus,x):
    err=[self.dist(i,x) for i in clus]
    return err.index(min(err))
  
  def group_mean(self,x,clus):
    clus_count=np.zeros(len(clus))
    error=0.0
    alot_x = [self.cluster(clus,i) for i in x]
    clus_sum =np.zeros((len(clus),len(x[0])))

    for i in range(len(x)) : 
      clus_sum[alot_x[i]]=clus_sum[alot_x[i]]+x[i]
      clus_count[alot_x[i]]+=1
      error+=self.dist(i,clus[alot_x[i]])

    error=error/len(x)
    new_clus =[clus_sum[i]/clus_count[i] for i in range(len(clus))]
    # print("\n","--- here are cal.new means","\n",new_clus,"\n")
    vv=np.array(new_clus)
    # plt.figure()        
    # plt.plot(x[:,0],x[:,1],".")  
    # plt.plot(vv[:,0],vv[:,1],"X")
    # plt.show()
    return new_clus,error
  
  def k_means_clustering(self,x,k,no_iter=11,p=0):
    m,n=x.shape
    initial_means=self.random_initialization(x,k,p)
    c=initial_means
    for i in range(no_iter): c,e=self.group_mean(x,c);print(i,e)
    vv=np.array(c)
    if p==1:
      plt.figure()        
      plt.plot(x[:,0],x[:,1],".")  
      plt.plot(vv[:,0],vv[:,1],"X")
      plt.show()
    return c,e