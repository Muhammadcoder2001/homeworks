users = {
    "Anvar" : 1,
    "Lobar" : 1,
    "Jasur" : 0,
    "Sodiq" : 0,
    "Hamid" :1
}
# Ovoz berganlar 1da chiqadi ovoz bermaganlar 0 da chiqadi.
num = int(input("1 yoki 0 kiriting: "))
for i, val in users.items():
    if val == num:
        print(i, end=' ')



