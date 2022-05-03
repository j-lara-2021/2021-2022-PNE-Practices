dic_l = {"A" : 2, "C": 5, "G": 7, "T":15}
max_val = 0
for v in dic_l.values():
    if v > max_val:
        max_val = v
    else:
        pass
print(f"most common base: {list(dic_l.keys())[list(dic_l.values()).index(max_val)]}")