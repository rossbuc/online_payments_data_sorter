import csv
from decouple import config
from difference_finder import difference_finder

API_PATH_PAYMENTS_FIRST_NAME = config('PATH_ONLINE_PAYMENTS')
API_PATH_PAYMENTS_DOT_COM = config('PATH_DOT_COM_PAYMENTS')



# ------ Data manipulation for the online payments -------

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
    if "," in entry[3]: 
        formatted_number = float(entry[3].replace(',', ''))
        result = '{:.2f}'.format(formatted_number/100)
        entry[3] = result

    print("this is the new entry 3, ", entry[3])
    sanitised_rows.append(entry)


    

sorted_data = sorted(sanitised_rows)
print(len(rows))

new_data = []
new_data_comparison = []

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
    del entry[0]
    entry.insert(0, full_name[1])
    entry.insert(0, full_name[0])
    new_data_comparison.append(entry)

print(len(header))

with open('Sanitised Payments Data.csv', 'w', newline='') as csvfile:
    fieldnames = ["Group Leader Last Name", "Group Leader First Name"] + header[1:]
    print(fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data)



# ------ Data manipulation for the Dot Com payments spreadsheet ------

rows_dot_com = []

with open(API_PATH_PAYMENTS_DOT_COM, "r") as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows_dot_com.append(row)

del rows_dot_com[:5]

for i, row in enumerate(rows_dot_com):
    del row[8]
    if row[0] == "Total remise:":
        print("I've found the row that says total remise, heres the proof, ", row, "and its at index, ", i)
        del rows_dot_com[i:]


sanitised_rows_dot_com = []

for entry in rows_dot_com:
    full_name = entry[7].split(" ")
    print(full_name)
    for i, name in enumerate(full_name): 
        for character in name:
            if not character.isalpha():
                print("Removing this character,", character, "from this name,", name)
                name = name.replace(character, '')
        full_name[i] = name
        if len(name) == 0:
            full_name.remove(name)
    by_last_name = "\xa0".join(full_name)
    print("this is the persons full name, ", full_name)
    entry[7] = by_last_name.capitalize()
    entry.insert(0, entry[7])
    del entry[8]
    sanitised_rows_dot_com.append(entry)

sorted_data_dot_com = sorted(sanitised_rows_dot_com)

print("this is the sorted data hopefully by alphabetical for dot com")
print(sorted_data_dot_com)

new_data_dot_com = []
new_data_dot_com_comparison = []

for entry in sorted_data_dot_com:
    full_name = entry[0].split("\xa0")
    entry_object_dot_com = {
        "Group Leader Last Name": full_name[0].capitalize(),
        "Group Leader First Name": full_name[1].capitalize(),
        "N°": entry[1],
        "Date/Heure": entry[2],
        "Amount (Montant)": entry[3],
        "Devise": entry[4],
        "Paiement": entry[5],
        "Magasin": entry[6],
        "Client": entry[7]
    }
    new_data_dot_com.append(entry_object_dot_com)
    del entry[0]
    entry.insert(0, full_name[1])
    entry.insert(0, full_name[0])
    new_data_dot_com_comparison.append(entry)


with open('Dot Com Sanitised Payments Data.csv', 'w', newline='') as csvfile:
    fieldnames = ["Group Leader Last Name", "Group Leader First Name", "N°", "Date/Heure", "Amount (Montant)", "Devise", "Paiement", "Magasin", "Client"]
    print(fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data_dot_com)

difference_finder(new_data_comparison, new_data_dot_com_comparison)