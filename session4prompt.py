class Cat:
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length = arm_length
		self.leg_length = leg_length 
		self.num_eyes = num_eyes 
		self.has_tail = has_tail 
		self.is_furry = is_furry 

	def describe_cat(self):
		print("physical characteristics of the cat:")
		print(f"length of arms: {self.arm_length} inches")
		print(f"length of legs: {self.leg_length} inches")
		print(f"number of eyes: {self.num_eyes}")
		print(f"has tail: {'yes' if self.has_tail else 'no'}")
		print(f"is furry: {'yes' if self.is_furry else 'no'}")

my_cat = Cat(5, 6, 2, True, True)

my_cat.describe_cat()

