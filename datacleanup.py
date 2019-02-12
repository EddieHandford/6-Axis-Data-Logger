    #this function is designed to clean up the data and linear interpolate
    #between the data points, outputs a x by 8 array
    
def dataCleanup (array):
        
    masterData = array
        
           
    masterDatav2 = [0 , 0 ,0 , 0 ,0 ,0 ,0 ,0]
    
    pairs = masterData.shape[0] -1
    i = 0
    p = 0
    x = 0
    row1 = []
    row2 = []
    item0 = 0
    item1 = 0 
    item2 = 0
    item3 = 0
    item4 = 0
    item5 = 0
    item6 = 0
    item7 = 0
    items = []
    
    #start of while loop
    while i <= (pairs - 1):
        
    
        row1 = masterData[i,:]
        row2 = masterData[i+1,:]
        
        np.transpose(row1)
        np.transpose(row2)    
        
        
        
        diff = row2[0] - row1[0]
     #   print(diff)
    
    
        if diff == 1 :
      
            masterDatav2 = np.concatenate([masterDatav2 , row1])        
            masterDatav2 = np.concatenate([masterDatav2 , row2])
        
            p = p+2
          #  print(masterDatav2)
        else:
            masterDatav2 = np.concatenate([masterDatav2 , row1]) 
            p = p+1
            x = 1
            while x < diff:    
                
                item0 = (row1[0] + x) # this column is milli, so does need linear interpolate
                
                item1= (((row2[1] - row1[1])*x)/diff) + row1[1]
                
                item2= (((row2[2] - row1[2])*x)/diff) + row1[2]
               
                item3= (((row2[3] - row1[3])*x)/diff) + row1[3]
               
                item4= (((row2[4] - row1[4])*x)/diff) + row1[4]
               
                item5= (((row2[5] - row1[5])*x)/diff) + row1[5]
               
                item6= (((row2[6] - row1[6])*x)/diff) + row1[6]
               
                item7= (((row2[7] - row1[7])*x)/diff) + row1[7]
               
             
                items = [item0 , item1 , item2 , item3 , item4 , item5 , item6 , item7 ]
               # np.transpose(items)
               # print(items)
                masterDatav2 = np.concatenate([masterDatav2 , items ])
                
                x = x+1  
                p = p+1
            
        if i == pairs:
                masterDatav2 = np.concatenate([masterDatav2 , row2 ])
    #    
       
        
        
        
        i = i+1
        
    masterDatapure = np.reshape(masterDatav2 , (   (p+1) ,   8    ))
    masterDatapure = np.delete(masterDatapure , (0), axis=0)
    return(masterDatapure)