n = int(input("Enter the length of the sequence: ")) # Do not change this line

first_num = 1
second_num = 2
third_num = 3
counter = 0

while counter < n:
    print(first_num)
    forth_num = first_num + second_num + third_num
        
    first_num = second_num
    second_num = third_num
    third_num = forth_num
    counter += 1