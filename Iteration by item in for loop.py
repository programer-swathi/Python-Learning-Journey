places=['madurai','krishnagiri','hosur','salem']
places.append('Dindugal')
print(places)
for place in places:
    if place =='krishnagiri':
        print("Yah its a place")
    else:
        print("No,it's not a place")

for x in range(len(places)):
    if places[x]=='salem':
        print("welcome")
    else:
        print("error")
