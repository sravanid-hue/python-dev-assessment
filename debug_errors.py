def calculate_average(numbers):
    total = 0

    try:
        for i in range(len(numbers)):
            total += numbers[i]

        return total / len(numbers)

    except ZeroDivisionError:
        print("Cannot calculate average of an empty list.")
        return None


def get_list_element(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        print("Error: Index is out of bounds.")
        return None

    except TypeError:
        print("Error: Input must be a list.")
        return None


# Example calls for calculate_average
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")



# Example calls for get_list_element
my_numbers = [100, 200, 300]

print("Valid index:", get_list_element(my_numbers, 1))
print("Invalid index:", get_list_element(my_numbers, 5))
print("Wrong type:", get_list_element("not a list", 1))