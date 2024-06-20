import numpy as np
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import pandapower as pp 
import math


import matplotlib.gridspec as gridscpec


pd.set_option('display.float_format', lambda x:'{:.4f}'.format(x))

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update(
    {
        'font.size':10,
        "text.usetex": False,
        "font.family": "serif",
        "font.sans-serif": ['Computer Modern'],
    }
)


net = pp.create_empty_network()
bus1 = pp.create_bus(net, vn_kv=110, name="Barra 1")
bus2 = pp.create_bus(net, vn_kv=220, name="Barra 2")
pp.create_load(net, bus2, p_mw=30, q_mvar=20, name="Carga 1A")
pp.create_line(net, bus1, bus2, length_km=500, std_type="NAYY 4x150 SE", name='L1')
pp.create_line(net, bus1, bus2, length_km=500, std_type="NAYY 4x50 SE", name='L2')
