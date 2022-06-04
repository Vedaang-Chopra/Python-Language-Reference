#  Yield keyword: - Used to create generator function
#  The generator is used in case of scale data. It is used to return data without using additional list.

# Example: -
def return_square(data):
    squared_data=[]
    for i in range(0,len(data)):
        squared_data.append(data[i]*data[i])
    return squared_data


def return_square_generator(data):
    for i in range(0,len(data)):
        yield(data[i]*data[i])

demo=[1,2,3,4,5,6]
new_data=return_square(demo)
print(new_data)

new_data_generator=return_square_generator(demo)
print(new_data_generator)

for i in new_data_generator:
    print(i)