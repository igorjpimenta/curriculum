import matplotlib.pyplot as plt
# import numpy as np

def pie_chart(labels, values, title):
    fig = plt.figure()
    fig.suptitle(title, fontsize=16, y=0.75)
    for i in range(0, len(labels)):
        fig.add_axes([i * 1/len(labels), 0, 1/len(labels), 1], aspect=1)
        plt.title(labels[i], fontsize=10, y=0.35)
        plt.pie([1 - values[i], values[i]], colors=['#EBE9F2', '#4B2283'], startangle=90)
        plt.gcf().gca().add_artist(plt.Circle((0,0), 0.7, color='#FFFFFF'))
        plt.text(0, 0.15, str(int(values[i] * 100)) + '%', horizontalalignment='center', verticalalignment='center', fontsize = 18, family = 'sans-serif')
    return plt.show()