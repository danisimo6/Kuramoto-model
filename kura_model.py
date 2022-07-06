import numpy as np
import matplotlib.pyplot as plt


class Kura:
    """
    """
    def __init__(self,N,K,dt):
        """
        """
        self.N = N
        self.K = K
        self.dt = dt
        
        self.theta = 2*np.pi*np.random.rand(N)
        self.omega = np.ones(N)
        self.A = np.ones((N,N))
        
        
    def forces(self):
        """
        """
        #return np.sum(self.A*np.sin(self.theta-self.theta.reshape(-1,1)),axis=1)
        return np.sum(self.A*(self.theta-self.theta.reshape(-1,1)),axis=1)
    
    def dynamics(self):
        """
        """
        self.theta += (self.omega + (self.K/self.N)*self.forces())*self.dt
        return self.theta
    
    def vis(self):
        
       
        ax.grid(zorder=9)
        ax.set_xlim([-2,2])
        ax.set_ylim([-2,2])
        ax.plot(np.cos(grid), np.sin(grid),zorder=11)
        ax.scatter(np.sum(np.cos(self.theta))/self.N,np.sum(np.sin(self.theta))/self.N,linewidths=10,zorder=13,color="black")
        for i in range(self.N):
            ax.scatter(np.cos(self.theta[i]),np.sin(self.theta[i]),linewidths=5,zorder=15)
        plt.draw()
        plt.pause(0.1)
            
            
N = 10
K = 1
dt = 0.05            
prova = Kura(N,K,dt)
fig, ax = plt.subplots(figsize=(12,12))
grid = np.arange(0,2*np.pi,0.01)

for i in range(200):
    theta = prova.dynamics()
    ax.grid(zorder=9)
    ax.set_xlim([-2,2])
    ax.set_ylim([-2,2])
    ax.plot(np.cos(grid), np.sin(grid),zorder=11)
    ax.scatter(np.sum(np.cos(theta))/N,np.sum(np.sin(theta))/N,linewidths=10,zorder=13,color="black")
    for i in range(N):
        ax.scatter(np.cos(theta[i]),np.sin(theta[i]),linewidths=5,zorder=15)
    plt.draw()
    plt.pause(0.05)
    ax.clear()
    