shopping_list = {
"piekarnia": ["chleb", "chalka"],
"warzywniak": ["pomidory", "cebula", "marchew", "ziemniaki"]
}

count = 0
for key, value in shopping_list.items():
    count += len(value)

for key, values in shopping_list.items():
    print(f"Idę do {key.capitalize()} i kupuję tam {[value.capitalize() for value in values]}.")
print(f"W sumie kupuję {count} produktów.")
hhhhh

