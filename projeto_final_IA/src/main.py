#!/usr/bin/env python

import utils
import random
import argparse
import signal
import sys
import tsp_ga as ga
import matplotlib.pyplot as plt
from datetime import datetime


def run(args):
    genes = utils.get_genes_from(args.cities_fn)

    if args.verbose:
        print("-- Running TSP-GA with {} cities --".format(len(genes)))

    history = ga.run_ga(genes, args.pop_size, args.n_gen,
                        args.tourn_size, args.mut_rate, args.verbose)

    if args.verbose:
      print("-- Drawing Route --")

    # Not plotting now
    # utils.plot(history['cost'], history['route'])

    if args.verbose:
        print("-- Done --")

def signal_handler(sig, frame):
    print('Exiting...')
    plt.close('all')
    print('Exited')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', type=int, default=1)
    parser.add_argument('--pop_size', type=int, default=700, help='Population size')
    parser.add_argument('--tourn_size', type=int, default=50, help='Tournament size')
    parser.add_argument('--mut_rate', type=float, default=0.02, help='Mutation rate')
    parser.add_argument('--n_gen', type=int, default=20, help='Number of equal generations before stopping')
    parser.add_argument('--cities_fn', type=str, default="data/map10.csv", help='CSV File containing the coordinates of cities')

    random.seed(datetime.now())
    args = parser.parse_args()

    if args.tourn_size > args.pop_size:
        raise argparse.ArgumentTypeError('Tournament size cannot be bigger than population size.')

    run(args)