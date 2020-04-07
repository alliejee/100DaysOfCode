# ex 8.14
def carmanker(manufacturer, model, **car_info):
    car_info['make'] = manufacturer
    car_info['model'] = model
    return car_info

car1 = carmanker('ford', 'pinto', color='green')
print(car1)