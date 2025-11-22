# main.py
# This is the main entry point for the SFPI calculator.
# It reads user input from the command line (like g(x), f(x), x0, tolerance, max iterations).
# Based on that input, it calls the solver modules:
#   - parser.py to turn the expression into a function
#   - transformer.py if the user gave f(x) and needs a fixed-point form
#   - convergence.py to check if the chosen g(x) will converge
#   - iteration.py to actually run the fixed-point iteration loop
#   - table.py to format and print the iteration results
# In short: main.py ties user input to the solver engine and shows the results back in the terminal.
