import csv
from decouple import config

API_PATH_PAYMENTS_FIRST_NAME = config('PATH_ONLINE_PAYMENTS')
rows = []

with open(API_PATH_PAYMENTS_FIRST_NAME, "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

sanitised_rows = []

for entry in rows:
    full_name = entry[0].split("\xa0")
    full_name.reverse()
    by_last_name = "\xa0".join(full_name)
    entry[0] = by_last_name.capitalize()
    sanitised_rows.append(entry)

    

sorted_data = sorted(sanitised_rows)
print(len(rows))

new_data = []

for entry in sorted_data:
    entry_object = {header[0]: entry[0], header[1]: entry[1], header[2]: entry[2], header[3]: entry[3], header[4]: entry[4], header[5]: entry[5], header[6]: entry[6], header[7]: entry[7], header[8]: entry[8], header[9]: entry[9], header[10]: entry[10], header[11]: entry[11]}
    print(entry_object)
    new_data.append(entry_object)

print(len(header))

with open('Sanitised Payments Data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(new_data)

