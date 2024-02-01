def reverse_array(arr):
    special_chars = {'&', '$', '%', '!', '@','#','$','^','*',')','(','-','+'}
    special_chars_positions = [i for i, char in enumerate(arr) if char in special_chars]
    reversed_arr = []
    reversed_special_chars_positions = []
    
    for i, char in enumerate(reversed(arr)):
        if i in special_chars_positions:
            reversed_special_chars_positions.append(len(reversed_arr))
            reversed_arr.append(char)
        elif char not in special_chars:
            reversed_arr.append(char)
    
    for i, position in enumerate(special_chars_positions):
        reversed_arr.insert(position, arr[position])
    
    return reversed_arr

arr = ['n', 2, '&', 'a', 'l', 9, '$', 'q', 47, 'i', 'a', 'j', 'b', 'z', '%', 8]
reversed_arr = reverse_array(arr)
print(reversed_arr)