def pifagor(sides: list) -> bool:
    sides.sort()
    return (sides[0]**2 + sides[1]**2 == sides[2]**2)
print(pifagor([5, 3, 4]))
print(pifagor([6, 8, 10]))
print(pifagor([100, 3, 65]))
