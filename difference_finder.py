import functools
# import pandas as pd

def difference_finder(data_set_online_payments, data_set_ski_dot_payments):

    unfound_entries = []

    for online_payment_entry in data_set_online_payments:
        online_payment_leader_last_name, online_payment_leader_first_name, _, _, online_payment_amount, *_ = online_payment_entry

        # Check if there is a corresponding entry in ski_dot_payments
        ski_dot_payment_found = any(
            online_payment_leader_last_name in ski_dot_entry 
            and float(online_payment_amount) == float(ski_dot_entry[4])
            for ski_dot_entry in data_set_ski_dot_payments
        )
        
        

        if not ski_dot_payment_found:
            unfound_entries.append(online_payment_entry)
            # print(online_payment_entry)

    print(type(data_set_ski_dot_payments[281][4]), " ", data_set_ski_dot_payments[281][4])
    print(type(data_set_online_payments[690][4]), " ", data_set_online_payments[690][4])
    print(float(data_set_ski_dot_payments[281][4]) == float(data_set_online_payments[690][4]))
    print(unfound_entries)
    return unfound_entries


