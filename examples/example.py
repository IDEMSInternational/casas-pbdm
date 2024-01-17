import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parents[1]))

from casas_pbdm.delay.basic import BasicDelay
from psymple.system import System

ants = BasicDelay("ants", n_bins = 10, rate = 1)

sys = System(ants)

sys.simulate(t_end = 10, n_steps = 10, mode = "discrete")

sys.plot_solution({f"x_ants_{i}" for i in range(10)})

