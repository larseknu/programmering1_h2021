def make_car(manufacturer, model, **options):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }

    for key, option in options.items():
        car[key] = option

    return car


def make_car_2(manufacturer, model, **options):
    options['manfucaturer'] = manufacturer
    options['model'] = model
    return options


volvo = make_car("Volvo", "V70", color='grey')
ferrari = make_car_2("Ferrari", "F430", color='red', electric=False, gear_type='manual', spoiler=True)

print(volvo)
print(ferrari)
