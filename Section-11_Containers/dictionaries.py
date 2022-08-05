#ssn_name_pairs = {}
#ssn_name_pairs["123-456-789"] = "John Appleseed"
#ssn_name_pairs["000-000-002"] = "Dwight Schrute"
#ssn_name_pairs["000-000-005"] = "Pam Beesly"

ssn_name_pairs = {"123-456-789": "John Appleseed", 
                  "000-000-002": "Dwight Schrute",
                  "000-000-003": "Pam Beesly"}

#print(ssn_name_pairs)
#print(ssn_name_pairs["000-000-003"])

#name = ssn_name_pairs["999-999-999"]

ssn_name_pairs["000-000-003"] = "Angela Martin"
ssn_name_pairs["000-000-006"] = "Andy Bernard"
#print(ssn_name_pairs)

#del ssn_name_pairs["000-000-002"]
#print(ssn_name_pairs)

key = "000-000-007"
if key in ssn_name_pairs:
    del ssn_name_pairs[key]
else:
    print(f"Invalid key {key}")