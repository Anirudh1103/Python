import matplotlib.pyplot as plt 
rainfall =  [17,9,16,3,21,7,8,4,6,21,4,1]
months = ['Jan','Feb','Mar','Apr','May','Jun',
'Jul','Aug','Sep','Oct','Nov','Dec']
plt.bar(months,rainfall,align='center',color = 'orange')
plt.show()