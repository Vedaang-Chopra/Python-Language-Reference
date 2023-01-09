# Generators..............
# They are computation technique, which doesn't hold everything in memory/ It yields(returns) one result at a time.
# It performs computation one result at a time. Have to fetch result one at a time.

#  Advantages: 
#  1. Code much more readable.
#  2. Memory advantage, since not all data is in memory

a=[1,2,3,4,5,6]

#  General Funcution to return square numbers..............
def square_numbers(nums):
    square=[]
    for i in nums:
        square.append(i*i)
    return square


squared_array=square_numbers(a)
print(squared_array)


#  Use of yield keyword, creates a generator
#  Yield keyword: - Used to create generator function
#  The generator is used in case of scale data. It is used to return data without using additional list.
# Example: -
def square_numbers_generator(nums:list):
    for i in nums:
        yield (i*i)

#  Result is a generator object.
generator_result=square_numbers_generator(a)
# To get the result from the generator object, we use the next keyword. It gives result one at time, how much time we run next
print(next(generator_result))
print(next(generator_result))
