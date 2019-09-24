# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(dict, title):
    labels, values = dict.values()
    fig = plt.figure(figsize=(7, 2))
    fig.suptitle(title, fontsize=16, y=1.05)
    for i in range(0, len(labels)):
        fig.add_axes([i * 1/len(labels), 0, 1/len(labels), 1], aspect=1)
        plt.title(labels[i], fontsize=12, y=0.35)
        plt.pie([1 - values[i], values[i]], colors=['#EBE9F2', '#4B2283'], startangle=90)
        plt.gcf().gca().add_artist(plt.Circle((0,0), 0.7, color='#FFFFFF'))
        plt.text(0, 0.15, str(int(values[i] * 100)) + '%', horizontalalignment='center', verticalalignment='center', fontsize = 20, family = 'sans-serif')
    return plt.show()

def scatter_plot(legend, dict, title, axis):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4.5))
    fig.suptitle(title, fontsize=16, y=0.97)
    color = [['#806437', '#FFE5BA', '#FFC76E', '#80725D', '#CCA057', '#CC9946'], ['#2A6980', '#A1E6FF', '#54D1FF', '#507380', '#43A6CB' ,'#8DBDCC']]
    for i, key, legend, color, xleg, yleg in zip([0, 1], dict, legend, color, [0.95, 0.9], [1.47, 1.47]):
        label, x, y = dict[key].values()
        x = np.array(x)
        y = np.array(y)
        for color, x, y, label in zip(color, x, y, label):
            label = label.split(' (')[0].split(' +')[0]
            axes[i].scatter(x, y, s=200, c=color, alpha=0.6, cmap='viridis', label=label)
            axes[i].annotate(label, xy=(x, y), xytext=(x-len(label)*0.01, y-0.07))#arrastar em x de acordo com a quantidade de caracteres
        axes[i].set_xlim(0, 1.1)
        axes[i].set_ylim(0, 1.1)
        axes[i].set_xlabel(axis[0])
        axes[i].set_ylabel(axis[1])
    return plt.show()