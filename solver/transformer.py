# Converts equations f(x)=0 into fixed-point form g(x).
# - Supports relaxation: g(x) = x - αf(x).
# - Can generate alternate rearrangements if the direct form diverges.
# Connects to: parser.py (to compile f(x)), iteration.py (to run the resulting g(x)).
