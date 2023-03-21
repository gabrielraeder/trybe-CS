def paint_cost(area):
    liters = area / 3
    cans = liters // 18
    if liters % 18:
        cans += 1

    return cans, f"R$ {cans * 80}0"


print(paint_cost(60))
