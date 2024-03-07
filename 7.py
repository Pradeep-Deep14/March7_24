#Nested List to List

def flattened_list(nested_list):
    Flattened = []
    for i in nested_list:
        if isinstance(i, list):
            Flattened.extend(flattened_list(i))
        else:
            Flattened.append(i)
    return Flattened

I = [1, 2, 3, [4, 5, 6], 7, 8]
result = flattened_list(I)
print("Flattened list: ", result)
