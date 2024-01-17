from psymple.populations import Population
from psymple.system import System

A = Population("A", initial_value=100)
B = Population("B", initial_value=1)

A._add_parameter("basic", "growth_A", "r", 0.1)
B._add_parameter("basic", "growth_B", "r", "-0.1")
A._add_update_rule("x_A", "r_growth_A * x_A")
B._add_update_rule("x_B", "r_growth_B * x_B")

AB = Population("AB")

AB._add_population(A)
AB._add_population(B)

AB._add_parameter("basic", "flow_AB", "f", 1)
AB._add_parameter("basic", "control_A", "c", 30)

AB._add_update_rule("x_A", "-f_flow_AB * x_A + c_control_A")
AB._add_update_rule("x_B", "f_flow_AB * (x_A - x_B)")

sys = System(AB)

for var in sys.variables:
    print(f"d({var.symbol})/dT = {var.update_rule.equation}")


