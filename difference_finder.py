import functools

def difference_finder(data_set_online_payments, data_set_ski_dot_payments):

    unfound_entries = []

    for entry in data_set_online_payments:
        online_payments_under_same_group_leader = any(entry[0] in sublist and any(entry[4] == x for x in sublist) for sublist in data_set_ski_dot_payments)
        print(online_payments_under_same_group_leader)
        if not online_payments_under_same_group_leader:
            unfound_entries.append(entry)
            print(entry)



