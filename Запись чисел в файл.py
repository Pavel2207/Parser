def create_file_with_numbers(n):
    x = open(f'range_{n}.txt', 'w')
    for i in range(1, n + 1):
        x.write(str(i)+'\n')
    x.close()
print(create_file_with_numbers(5))