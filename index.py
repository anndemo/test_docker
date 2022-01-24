import csv

with open('./data/logs.csv', 'r+') as file:
    num_lines = 0
    print("Zero!!!")
    for line in file.readlines():
        num_lines += 1
        print(f"Hello, {num_lines} times!")
    writer = csv.writer(file)
    writer.writerow([f"{num_lines+1}"])

