import numpy as np 

def generate_sin_table():
	print("x\tsin(x)")
	x_values = np.linspace(0, 2, num=1000)
	sin_values = np.sin(x_values)
	for x, sin_x in zip(x_values, sin_values):
		print(f"{x}\t{sin_x}")

def main():
	generate_sin_table()

if __name__ == "__main__":
	main() 