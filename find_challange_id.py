from utils import generate_challange, generate_seed
import random
max_values = 999
form_digit = random.choice([1, 2, 3])
rest = random.randint(1, max_values) 
random_seed = (1 * 10000) + (form_digit * 1000) + rest

# for x in range(1000):
#     random_seed = x
#     result = generate_challange(random_seed)
#     if (result['Format'] == "Single Shot" and result['Orientation'] == "Square" and result['Theme'] == "Geometry" and result['Color'] == 'Black & white'
#     ):
#         print(result)
#         print(random_seed)
#         print(" - - - - -- - - -- - - - - - - -- -  ")
#print(random_seed)
seed = 32224
id = generate_seed()
print(id)
challange = generate_challange(id)
print(challange)