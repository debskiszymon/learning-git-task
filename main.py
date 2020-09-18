shopping_list = {
"piekarnia": ["chleb", "chalka"],
"warzywniak": ["pomidory", "cebula", "marchew", "ziemniaki"]
}

#shopping_list1 = {}

#for key, values in shopping_list.items():
#    for z in values:
#        shopping_list[key].append(z)
#
#print(shopping_list)

count = 0
for key, value in shopping_list.items():
    count += len(value)

for key, values in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[value.capitalize() for value in values]}.")
print(f"W sumie kupuję {count} produktów.")

