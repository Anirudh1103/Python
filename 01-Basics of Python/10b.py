import matplotlib.pyplot as plt
labels = ['Chrome','Internet explorer','Firefox','edge','Safari','Others']
marketshare = [60.6,5.5,15.0,10.5,2,6.5]
explode = (0.1,0,0,0,0,0)
plt.pie(marketshare,explode=explode,labels = labels,autopct="%.1f%%",shadow = True, startangle= 45)
plt.title("Market share")
plt.show()