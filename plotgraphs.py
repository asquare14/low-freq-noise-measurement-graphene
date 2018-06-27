
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_graph():
    headers = ['X-Axis', 'Y-Axis', 'None']
    df = pd.read_csv ('./Values.csv', names =headers)
    #print df

    x = df['X-Axis']
    y = df['Y-Axis']

    plt.xlabel("X-Axis", fontsize = 15, color = 'green')
    plt.ylabel("Y-Axis", fontsize = 15, color = 'green')
    plt.title("Graph", fontsize = 22, color = 'red')

    plt.plot(x,y)
    plt.grid(True)
    plt.axhline(y = 0, color = 'yellow', alpha = 0.3)
    plt.axvline(x = 0, color = 'yellow', alpha = 0.3)
    plt.gcf().autofmt_xdate()
    plt.show()
