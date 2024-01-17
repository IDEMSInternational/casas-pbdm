from psymple.populations import Population, IndexedPopulation
from psymple.variables import Parameter

class BasicDelay(IndexedPopulation):
    def __init__(self, name, n_bins = 10, rate = 0, initial_value = 1000):
        super().__init__(name, (n_bins,))
        flow = Parameter.basic(f"({name}-flow)", "f", rate)
        self.parameters += flow
        for i in range(n_bins):
            self.add_population(Population(f"{name}_{i}", initial_value = (initial_value if i == 0 else 0)), i)
            equation = (flow.symbol * self[i-1].variable.symbol if i > 0 else 0) - (flow.symbol * self[i].variable.symbol)
            self._add_update_rule(self[i].variable, equation)


# Basic delay means single flow rate throughout. A (NonBasic)Delay would allow for rates to be specified as an array.
