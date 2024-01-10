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
    for i, name in enumerate(full_name): 
        for character in name:
            if not character.isalpha():
                print("Removing this character,", character, "from this name,", name)
                name = name.replace(character, '')
        print(name)
        full_name[i] = name
    by_last_name = "\xa0".join(full_name)
    entry[0] = by_last_name.capitalize()
    sanitised_rows.append(entry)


    

sorted_data = sorted(sanitised_rows)
print(len(rows))

new_data = []

for entry in sorted_data:
    full_name = entry[0].split("\xa0")
    entry_object = {
        "Group Leader Last Name": full_name[0].capitalize(),
        "Group Leader First Name": full_name[1].capitalize(),
        header[1]: entry[1],
        header[2]: entry[2], 
        header[3]: entry[3], 
        header[4]: entry[4], 
        header[5]: entry[5], 
        header[6]: entry[6], 
        header[7]: entry[7], 
        header[8]: entry[8], 
        header[9]: entry[9], 
        header[10]: entry[10], 
        header[11]: entry[11]
        }
    new_data.append(entry_object)

print(len(header))

with open('Sanitised Payments Data.csv', 'w', newline='') as csvfile:
    fieldnames = ["Group Leader Last Name", "Group Leader First Name"] + header[1:]
    print(fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data)

