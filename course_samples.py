"""
This files contains all samples required for D&A Academy
"""
# Lesson 1: Introduction to Python
# Objective: Introduce Python and its basic syntax.

# 1. Print "Hello, world!" using the `print()` function.
print("Hellos world!")

# 2. Declare variables and assign values of different data types (e.g., string, integer, float).
samples = ['9', 9, 9., 8+9j]

# 3. Perform arithmetic operations (+, -, *, /) using variables.
print(" + operand: {}".format(samples[2] + 3))
print(" - operand: {}".format(samples[2] - 3))
print(" * operand: {}".format(samples[2] * 3))
print(" / operand: {}".format(samples[2] / 3))


# 4. Use comments to add explanations to your code.
# Already did

# 5. Explore Python's built-in functions (e.g., `len()`, `type()`) and use them in simple programs.
for sample in samples:
	print(type(sample))