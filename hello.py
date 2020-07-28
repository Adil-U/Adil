# spisok
names = ["Adil","Harry", "Potter"]

names.append("Draco")

names.sort()
print (names)
# mnozhestva
s = set()

# insert massyv dannyh
i = 0 
n = int(input("Vvedite chislo do kotorogo budet massiv: "))
while i < n:
	s.add(i+1)
	i = i + 1

print(s)
print (f"The set has {len(s)} elements")