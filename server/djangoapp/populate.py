from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "Audi", "description": "German luxury car manufacturer"},
        {"name": "Toyota", "description": "Japanese car manufacturer"},
        {"name": "Honda", "description": "Japanese car manufacturer"},
        {"name": "Ford", "description": "American car manufacturer"},
        {"name": "BMW", "description": "German luxury car manufacturer"},
        {"name": "Nissan", "description": "Japanese car manufacturer"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'], description=data['description']))

    car_model_data = [
        {"name": "A6", "type": "Sedan", "year": 2020,
         "dealer_id": 15, "car_make": car_make_instances[0]},
        {"name": "Q5", "type": "SUV", "year": 2021,
         "dealer_id": 15, "car_make": car_make_instances[0]},
        {"name": "Corolla", "type": "Sedan", "year": 2019,
         "dealer_id": 3, "car_make": car_make_instances[1]},
        {"name": "RAV4", "type": "SUV", "year": 2022,
         "dealer_id": 3, "car_make": car_make_instances[1]},
        {"name": "Civic", "type": "Sedan", "year": 2020,
         "dealer_id": 29, "car_make": car_make_instances[2]},
        {"name": "CR-V", "type": "SUV", "year": 2021,
         "dealer_id": 29, "car_make": car_make_instances[2]},
        {"name": "Mustang", "type": "Coupe", "year": 2018,
         "dealer_id": 5, "car_make": car_make_instances[3]},
        {"name": "Explorer", "type": "SUV", "year": 2022,
         "dealer_id": 5, "car_make": car_make_instances[3]},
        {"name": "X5", "type": "SUV", "year": 2023,
         "dealer_id": 10, "car_make": car_make_instances[4]},
        {"name": "Altima", "type": "Sedan", "year": 2020,
         "dealer_id": 12, "car_make": car_make_instances[5]},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'], car_make=data['car_make'],
            type=data['type'], year=data['year'],
            dealer_id=data['dealer_id'])
