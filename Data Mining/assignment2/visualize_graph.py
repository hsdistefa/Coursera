from __future__ import print_function

import os

import matplotlib.pyplot as plt
import networkx as nx
from six.moves.urllib.request import urlretrieve


def maybe_download(url, dest):
    _, filename = os.path.split(dest)
    if not os.path.exists(dest):
        print('Downloading:', filename)
        filename, _ = urlretrieve(url, dest)
        print('Download Complete!')
    else:
        print('File Found')


def visualize_graph(gml_filepath):
    G = nx.read_gml(gml_filepath)
    nx.draw(G, node_color='#A0CBE2', edge_color='#1104FF')
    plt.show()


if __name__ == '__main__':
    URL = 'http://networkdata.ics.uci.edu/data/celegansneural/celegansneural.gml'
    DATA_ROOT = './data'
    filename = URL.split('/')[-1]
    dest = os.path.join(DATA_ROOT, filename)

    maybe_download(URL, dest)
    visualize_graph(dest)
