import matplotlib.pyplot as plt 

x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]


plt.scatter(x,y,label='skitscat',color='c',marker='*')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting value \nCheck it out')
plt.legend()
plt.show( )	