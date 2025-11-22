# Checks if the chosen g(x) is likely to converge.
# - Estimates |g’(x)| numerically.
# - Warns if |g’(x)| ≥ 1 (risk of divergence).
# - Detects oscillation or cycles in iteration.
# - Can adjust damping (lambda) to stabilize iteration.
# Connects to: iteration.py (used before and during iteration), advisor.py (to suggest alternatives).
