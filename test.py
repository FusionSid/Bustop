a = [
    [('Andrew',), (None,), ('Alex',), ('Amanda',), (None,), (None,),('Abhijit',)],
    [(None,), (None,), (None,), (None,), ('Apple',), (None,), (None,)],
    [(None,), (None,), (None,), (None,), (None,), (None,), (None,)],
    [(None,), ('Amber',), (None,), (None,), (None,), ('Aqua',), (None,)],
    [(None,), (None,), (None,), (None,), (None,), (None,), (None,)],
    [(None,), (None,), (None,), (None,), (None,), (None,), (None,)]
    ]

letter = "a"
ans = []

for item in a:
    i1 = item
    for item in i1:
        try:
            if item[0][0].lower == letter.lower():
                print(':)')
        except:
            pass
        else:
            ans.append(item[0])
print(ans)
for x in ans:
    print ("".join(x)+"")