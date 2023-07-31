# Create a program that generates a password of 6 random alphanumeric characters
# from "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

import random

sequence = """abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"""

print(''.join(random.sample(sequence, 6)))
