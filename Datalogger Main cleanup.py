# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:22:31 2019

@author: ED
"""

import numpy as np;
from scipy import interpolate
import pylab as py


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation  as animation
from matplotlib import style
from matplotlib.animation import FuncAnimation,FFMpegFileWriter



#import data from Master logger
masterData = np.genfromtxt("MASTER.txt" ,  delimiter= ',' ) ;
masterData = np.delete(masterData , (0) , axis=0 )


#-----------------A list of what each column is---------------------#

#f0         time in milliseconds
#f1         acceleration in x
#f2         acceleration in y
#f3         acceleration in z
#f4         gyro x
#f5         gyro y
#f6         gyro z
#f7         FSR ( note , 0 to 20N = 0 to 900 ish)

#note the time that the Master began logging, used to sync all slave devices

offsetTime = masterData[0,0];
print(offsetTime)






      
#import data from SlaveB
slaveBdata = np.genfromtxt("SLAVEB.txt" ,  delimiter= ',' ) ;
slaveBdata = np.delete(slaveBdata , (0) , axis=0 );
slaveBbeginTime = slaveBdata[0,0];
print(slaveBbeginTime)



#import data from SlaveC
slaveCdata = np.genfromtxt("SLAVEC.txt" ,  delimiter= ',' ) ;
slaveCdata = np.delete(slaveCdata , (0) , axis=0 );
slaveCbeginTime = slaveCdata[0,0];
print(slaveCbeginTime)


    
 


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('loaded.jpg')
imgplot = plt.imshow(img)
plt.show()

    
#now need to correct all the slaves timings
    
    

     
    
slaveBcorrection = slaveBbeginTime - offsetTime;
slaveBdata[: , 0] = slaveBdata[: , 0] - slaveBcorrection;
   

slaveCcorrection = slaveCbeginTime - offsetTime;
slaveCdata[: , 0] = slaveCdata[: , 0] - slaveCcorrection;

masterData[:,0] = masterData[:,0] - offsetTime
slaveBdata[:,0] = slaveBdata[:,0] - offsetTime
slaveCdata[:,0] = slaveCdata[:,0] - offsetTime


    
for i in range (6):

    masterData[: , i+1] = masterData[: , i+1] - (np.median(masterData[: , i+1]) ) ;


for i in range (6):
    
    slaveBdata[: , i+1] = slaveBdata[: , i+1] - (np.median(slaveBdata[: , i+1]) ) ;
    

for i in range (6):
    
    slaveCdata[: , i+1] = slaveCdata[: , i+1] - (np.median(slaveCdata[: , i+1]) ) ;


    
masterDatapure = dataCleanup(masterData)
print('file 1 cleanup complete')
slaveBdataPure = dataCleanup(slaveBdata)
print('file 2 cleanup complete')
slaveCdataPure = dataCleanup(slaveCdata)
print('file 3 cleanup complete')











##now all the data has been smoothed , we are ready to start viewing the data

#style.use('fivethirtyeight')
##
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ani = animation.FuncAnimation(fig, animate(masterDatapure , 2) , interval=1)
#plt.show

#masterDatapure[:,0], masterDatapure[:,1]





    
    
    
    
    
    



plt.plot(masterData[: , 0] , masterData[:,1])
plt.plot(masterData[:, 0] , masterData[:,2])
plt.show


#
#fig, ax = plt.subplots()
#xdata, ydata = [] , []
#ln, = plt.plot([], [], 'r', animated=True)
#f = np.linspace(-3, 3, 200)
#
#def init():
#	ax.set_xlim(0, 60000)
#	ax.set_ylim(-0.5, 0.5)
#	ln.set_data(xdata,ydata)
#	return ln,
#
#
#def update(frame):
#	xdata.append(frame)
#	ydata.append(np.exp(-frame**2))
#	ln.set_data(xdata, ydata)
#	return ln,
#
#ani = FuncAnimation(fig, update, frames=f,
#                    init_func=init, blit=True, interval = 2.5,repeat=False)
#plt.show()









#ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()





#
#
#while i<= pairs :
#    
#    row1 = masterData[:,i]
#    row2 = masterData[:,i+1]
#    diff = row2[1] - row1[1]
#    print(diff)
#    




#
#plt.plot(masterData[: , 0] , masterData[:,1])
#plt.show





#
#plt.plot(masterData[7000:8000 , 2], masterData[7000:8000, 16])
#plt.show()
#plt.plot(slaveBdata[5000:5500 , 2] , slaveBdata[5000:5500 , 10] )
#
##plt.plot(slaveCdata[: , 2] , slaveCdata[: , 10] )
#
#plt.plot(masterData[7000:8000 , 2] , masterData[7000:8000 , 10] )
#plt.show()

#
#plt.plot(slaveBdata[: , 2] , slaveBdata[: , 14] )
#plt.plot(slaveCdata[: , 2] , slaveCdata[: , 14] )
#plt.plot(masterData[: , 2] , masterData[: , 14] )
#plt.show()



#plt.plot(slaveBdata[10:100 , 2] , slaveBdata[10:100 , 8] )
#plt.plot(slaveCdata[10:100 , 2], slaveCdata[10:100 , 8] )
#plt.plot(masterData[10:100 , 2], masterData[10:100 , 8] )
#plt.show()

        

