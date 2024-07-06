def my_sort(sonlar):
    if not all(isinstance(son, int) and son > 0 for son in sonlar):
        raise ValueError("Barcha elementlar faqat musbat butun sonlar bo'lishi kerak.")
    
    def xonalar_yigindisi(son):
        return sum(int(xona) for xona in str(son))
    
    saralangan_sonlar = sorted(sonlar, key=xonalar_yigindisi)
    
    return saralangan_sonlar

lst = [55, 12, 34, 103]
print(my_sort(lst))
