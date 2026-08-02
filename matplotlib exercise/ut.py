import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures = [30, 32, 45, 55, 65, 75, 85, 80, 70, 60, 50, 35]
plt.plot(months, temperatures, marker='o', color='green', linestyle='-')
plt.title('Average Monthly Temperatures')
plt.xlabel('Month') 
plt.ylabel('Temperature (°F)')
plt.grid(True)
plt.show()
