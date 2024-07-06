print("Ranglar soni  yetarli bo'lsa nolni bosib to'xtating: ")
colors =list()
while True:
    color = input("Enter color name: ") 
    if color == '0':
        break
    else:
        colors.append(color)
print(colors)
length = len(colors)
if length == 1:
    print(2)
else:
    result = length * 2 + (length-1)
    print("Shuncha soniyada bo'yab olasiz!!! ",result)


