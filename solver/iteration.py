# Runs the fixed-point iteration loop: x_{k+1} = g(x_k).
# - Tracks error using ε_a = |(x_{k+1} - x_k)/x_{k+1}| * 100%.
# - Stops when error < tolerance or max iterations reached.
# - Supports optional Aitken acceleration for faster convergence.
# Connects to: convergence.py (for derivative checks), table.py (to format results).
