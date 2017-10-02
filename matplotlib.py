# Prints 11 different types of charts using matplotlib and numpy

import matplotlib.pyplot as plt

#Line Graph

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label ="First Line")
plt.plot(x2, y2, label = "Second Line")
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# Bar Chart

plt.bar([1,3,5,7,9],[5,2,7,8,2], label = 'Example one', color='b')
plt.bar([2,4,6,8,10],[8,6,2,5,6], label = 'Example two', color='g')
plt.legend()
plt.xlabel('Bar Number')
plt.ylabel('Bar Height')

plt.title('Super Epic Graph\nAnother Line!')
plt.show()

#Histogram

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Histogram\nCheck it out')
plt.legend()
plt.show()


# Scatter Plot

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='scatterplot', color='k', s=25, marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Scatterplot\nCheck it out')
plt.legend()
plt.show()


#Stack Plot

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot Graph\nCheck it out')
plt.legend()
plt.show()



# Pie Chart

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%'
        )
plt.title('Pie Chart\nCheck it out')
plt.show()



#Importing data from a file

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data.txt','r') as csvfile:
#Imported files doesn't have to be a csv - it can be any delimited file.
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

#Importing files with NumPy is even better?

import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


#Importing data from the interwebz!

import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y%m%d')})

    ax1.plot_date(date, closep, '-', label='Price')

    ax1.plot([], [], linewidth=5, label='loss', color='r', alpha=0.5)
    ax1.plot([], [], linewidth=5, label='gain', color='g', alpha=0.5)

    ax1.fill_between(date, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.5)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.set_yticks([0, 25, 50, 75])
    ax1.spines['left'].set_color('c')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_linewidth(2)
    ax1.tick_params(axis='x', colors='#f06215')
    ax1.axhline(closep[0], color='k', linewidth='1')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('EBAY')


# Continuously updating graphs using matplotlib's animation module

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure() # Top level container for all plot elements
ax1 = fig.add_subplot(1,1,1)

# Animation function below

def animate(i):
    graph_data = open('data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()


#Subplots - Basically additional plots inside of a figure. Three numbers are height, width, plot number
import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys

#ax1 = fig.add_subplot(221) #2 tall, 2 wide, plot number 1
#ax2 = fig.add_subplot(222) #2 tall, 2 wide, plot number 2
#ax3 = fig.add_subplot(212) #2 tall, 1 wide, plot number 1

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1) # 6 tall, 1 wide, starting point is 0,0
ax2 = plt.subplot2grid((6,1), (2,0), rowspan=2, colspan=1)
ax3 = plt.subplot2grid((6,1), (4,0), rowspan=1, colspan=1)

x,y = create_plots()
ax1.plot(x,y)

x,y = create_plots()
ax2.plot(x,y)

x,y = create_plots()
ax3.plot(x,y)


plt.show()
