attendance = [18, 20, 19, 15, 21]
full_day=0
total_attendence=0
for day in attendance:
    if day >=20:
        print("full")
        full_day+=1
    else:
        print("not full") 
    total_attendence+=day   
print("Total attendence:",total_attendence)
print("Number of days:",full_day)