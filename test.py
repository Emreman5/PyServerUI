import time
import matplotlib.pyplot as plt

x = [0,100,200]
y = [0,200,0]
plt.ion()
colors = ['b','b','b']
norm = plt.Normalize(1, 4)
cmap = plt.cm.PiYG

fig, ax = plt.subplots()
scatter = plt.scatter(
    x=x,
    y=y,
    c=colors,
    s=100,
    cmap=cmap,
    norm=norm
)
plot1, = ax.plot((100), (100), 'o', color='r')
plot2, = ax.plot((100), (100), 'o', color='purple')
annotation = ax.annotate(
    text='',
    xy=(0, 0),
    xytext=(15, 15),
    textcoords='offset points',
    bbox={'boxstyle': 'round', 'fc': 'w'},
)
for i, j in zip(x, y):
    plt.annotate('(%.1f, %.1f)' % (i, j), xy=(i, j), textcoords='offset points', xytext=(0,10), ha='center')

plt.text(-5, 195, 'Beacon', fontsize = 14, bbox = dict(facecolor = 'blue', alpha = 1), color = 'w')
plt.text(-5, 180, 'Filtrelenmiş Konum', fontsize = 14, bbox = dict(facecolor = 'red', alpha =1), color = 'w')
plt.text(-5, 165, 'Gerçek Konum', fontsize = 14, bbox = dict(facecolor = 'purple', alpha =1), color = 'w')
plot1.set_markersize(10)
plot2.set_markersize(10)

count = 100
for _ in range(100000):
    plot1.set_ydata(count)
    plot1.set_xdata(count)
    plot2.set_ydata(count)
    ann = plt.annotate('(%.1f, %.1f)' % (count, count), xy=(count, count), textcoords='offset points', xytext=(0,10), ha='center')
    count+= 1
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)
    ann.remove()
    
