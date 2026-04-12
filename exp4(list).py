#list operation
#4.1
legends = ["Messi", "Ronaldo", "Neymar"]
print("Initial Legends:", legends)

legends.insert(1, "Mbappe")
print("After Inserting Mbappe at index 1:", legends)

young_stars = ["Lamine Yamal", "Haaland"]
legends.extend(young_stars)
print("After Extending:", legends)

legends.reverse()
print("After Reversing:", legends)

legends.remove("Ronaldo")
print("After removing Ronaldo:", legends)

del legends
print("List cleared successfully.")


#4.2
jn=[4,7,10,9]
even_jn=[]
for i in jn:
  if i%2==0:
    even_jn.append(i)

print("Even Jersey Numbers:",even_jn)


#4.3
jn=[1,2,3,4,7,10]
jn2=[4,7,10]
common=[]
for i in jn:
  if i in jn2:
    common.append(i)

print("Common Jersey Numbers:",common)