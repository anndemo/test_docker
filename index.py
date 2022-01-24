# import csv
#
# with open('./data/logs.csv', 'r+') as file:
#     num_lines = 0
#     print("Zero!!!")
#     for line in file.readlines():
#         num_lines += 1
#         print(f"Hello, {num_lines} times!")
#     writer = csv.writer(file)
#     writer.writerow([f"{num_lines+1}"])


from uuid import uuid4
from storage import MongodbService
import time

storage = MongodbService.get_instance()

print("Zero!!!")
num = 0
for data in storage.get_data():
    num += 1
    print(data['string'])


hello = {
    "_id": str(uuid4()),
    "time": str(int(time.time())),
    "string": f"Hello, {num+1} times!"
}
storage.save_data(hello)
