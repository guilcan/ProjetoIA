import matplotlib.pyplot as plt
import tsp_ga as ga
import pandas as pd
import math
from random import sample
from mpl_toolkits.basemap import Basemap


def get_genes_from(fn, sample_n=0):
    df = pd.read_csv(fn)
    genes = [ga.Gene(row['city'], row['x'], row['y'])
             for _, row in df.iterrows()]

    # return genes if sample_n <= 0 else sample(genes, sample_n)
    return genes


def plot(costs, individual, save_to=None):
    plt.figure(1)
    plt.subplot(121)
    plot_ga_convergence(costs)

    plt.subplot(122)
    plot_route(individual)

    if save_to is not None:
        plt.savefig(save_to)
        plt.close()
    else:
        plt.show()

def plot_ga_convergence(costs):
    x = range(len(costs))
    plt.title("GA Convergence")
    plt.xlabel('generation')
    plt.ylabel('cost (KM)')

    plt.text(x[len(x) // 2], costs[0], 'min cost: {:.2f} KM'.format(costs[-1]), ha='center', va='center')
    plt.plot(x, costs, '-')


def plot_route(individual):
    m = Basemap(projection='cyl', resolution=None)

    plt.axis('on')
    plt.grid(True)
    plt.title("Shortest Route")

    seq = ""
    for i in range(0, len(individual.genes)):
        origin_name = individual.genes[i].name
        x = individual.genes[i].x
        y = individual.genes[i].y

        plt.plot(x, y, 'ok', c='r', marker='o')
        if i == len(individual.genes) - 1:
            dest_name = individual.genes[0].name
            x2 = individual.genes[0].x
            y2 = individual.genes[0].y
        else:
            dest_name = individual.genes[i+1].name
            x2 = individual.genes[i+1].x
            y2 = individual.genes[i+1].y

        distance =  math.sqrt(pow(x - x2, 2) + pow(y - y2, 2))
        if origin_name or not math.isnan(origin_name):
          print("{} ({},{})".format(origin_name, x, y))
          seq += origin_name 
          if i == len(individual.genes) - 1:
            seq += dest_name

        plt.plot([x, x2], [y, y2], 'k-', c='r', marker='o')

    print(seq)