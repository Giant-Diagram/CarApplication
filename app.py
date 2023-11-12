from functools import reduce
from typing import List, Dict

from flask import Flask, request, jsonify

# Erstelle eine Flask-App
app_instance = Flask(__name__)


@app_instance.route('/', methods=['GET'])
def index():
    return "Welcome to the Car Application" \
           "Please use the following endpoints:" \
           "/A1G, /A1F, /A1E, /B1F, /B1E, /B2G, /B2F, /B2E, /B3G, /B3F, /B3E, /B4G, /B4F, /B4E"


# Endpunkt /A1G
@app_instance.route('/A1G', methods=['GET'])
def a1g():
    # Funktion als pure function: Abhängig nur von den Eingabeparametern
    def calculate_discount(price):
        return price * 0.9

    return jsonify({"result": calculate_discount(10000)})


# Endpunkt /A1F
@app_instance.route('/A1F', methods=['GET'])
def a1f():
    # Verwendung von immutable values für Autonamen
    car_name = "audi"
    uppercase_name = car_name.upper()
    return jsonify({"result": uppercase_name})


# Endpunkt /A1E
@app_instance.route('/A1E', methods=['GET'])
def a1e():
    car_data = [
        {'brand': 'Toyota', 'model': 'Camry', 'price': 16000},
        {'brand': 'Honda', 'model': 'Accord', 'price': 18000},
        {'brand': 'Ford', 'model': 'Fusion', 'price': 14000}
    ]
    
    # Funktionale Lösung für die Filterung teurer Autos
    def filter_expensive_cars(car_data):
        return list(filter(lambda car: car['price'] > 15000, car_data))

    return jsonify({"result": filter_expensive_cars(car_data)})


# Endpunkt /B1F
@app_instance.route('/B1F', methods=['GET'])
def b1f():
    car_data = [
        {'brand': 'Toyota', 'model': 'Camry', 'price': 16000},
        {'brand': 'Honda', 'model': 'Accord', 'price': 18000},
        {'brand': 'Ford', 'model': 'Fusion', 'price': 14000}
    ]

    # Funktion zur Überprüfung, ob ein Auto teuer ist
    def is_expensive(car):
        return car['price'] > 15000

    # Funktion zur Filterung von teuren Autos
    def filter_expensive_cars(car_data):
        return list(filter(is_expensive, car_data))

    return jsonify({"result": filter_expensive_cars(car_data)})


# Endpunkt /B1E
@app_instance.route('/B1E', methods=['GET'])
def b1e():
    car_data = [
        {'brand': 'Toyota', 'model': 'Camry', 'price': 16000},
        {'brand': 'Honda', 'model': 'Accord', 'price': 18000},
        {'brand': 'Ford', 'model': 'Fusion', 'price': 14000}
    ]

    def is_expensive(car):
        return car['price'] > 15000

    # Funktion zur Filterung von teuren Autos
    def filter_expensive_cars(car_data):
        return list(filter(is_expensive, car_data))

    # Gesamtalgorithmus zur Filterung teurer Autos
    def main_algorithm(car_data):
        expensive_cars = filter_expensive_cars(car_data)
        # Weitere Verarbeitung oder Ausgabe der teuren Autos
        return expensive_cars

    return jsonify({"result": main_algorithm(car_data)})


# Endpunkt /B2G
@app_instance.route('/B2G', methods=['GET'])
def b2g():
    # Funktion zur Berechnung des Rabatts auf Autopreise
    def calculate_discount(price):
        return price * 0.9

    # Funktion als Objekt in Variable speichern
    discount_function = calculate_discount

    # Anwendung der Funktion auf eine Liste von Autopreisen
    car_prices = [5000, 8000, 12000, 15000]
    discounted_prices = list(map(discount_function, car_prices))
    return jsonify({"result": discounted_prices})


# Endpunkt /B2F
@app_instance.route('/B2F', methods=['GET'])
def b2f():
    car_prices = [5000, 8000, 12000, 15000]

    # Funktion zur Filterung von Autos basierend auf Rabatt
    def filter_expensive_cars(price, filter_function):
        return filter_function(price > 10000)

    # Funktion für die Anwendung des Rabattfilters auf Autopreise
    def apply_discount_filter(price):
        return price * 0.9

    # Anwendung der Funktion mit Rabattfilter auf eine Liste von Autopreisen
    expensive_cars = list(filter(lambda price: filter_expensive_cars(price, apply_discount_filter), car_prices))
    return jsonify({"result": expensive_cars})


# Endpunkt /B2E
@app_instance.route('/B2E', methods=['GET'])
def b2e():
    car_prices = [5000, 8000, 12000, 15000]

    # Funktion zur Erzeugung von Rabattfunktionen mit einem bestimmten Faktor
    def create_discount_function(factor):
        def discount_function(price):
            return price * factor

        return discount_function

    # Erzeugung von Rabattfunktionen mit verschiedenen Faktoren
    discount_10_percent = create_discount_function(0.9)
    discount_15_percent = create_discount_function(0.85)

    # Anwendung von Rabattfunktionen auf eine Liste von Autopreisen
    discounted_prices_10_percent = list(map(discount_10_percent, car_prices))
    discounted_prices_15_percent = list(map(discount_15_percent, car_prices))
    return jsonify(
        {"result_10_percent": discounted_prices_10_percent, "result_15_percent": discounted_prices_15_percent})


# Endpunkt /B3G
@app_instance.route('/B3G', methods=['GET'])
def b3g():
    # Lambda für das Quadrieren einer Autopreisliste
    car_prices = [5000, 8000, 12000, 15000]
    squared_prices = list(map(lambda price: price ** 2, car_prices))

    # Lambda für das Konvertieren von Autonamen zu Großbuchstaben
    car_names = ['audi', 'bmw', 'mercedes']
    uppercase_names = list(map(lambda name: name.upper(), car_names))
    return jsonify({"result": uppercase_names})


# Endpunkt /B3F
@app_instance.route('/B3F', methods=['GET'])
def b3f():
    # Lambda für die Filterung schwarzer Autos mit Preisen über 10000
    car_data = [{'color': 'black', 'price': 8000}, {'color': 'blue', 'price': 12000},
                {'color': 'black', 'price': 10000}]
    filtered_black_cars = list(filter(lambda car: car['color'] == 'black' and car['price'] > 10000, car_data))

    # Lambda für die Berechnung des Rabatts auf Basis von Autopreis und Kilometerstand
    discounted_prices = list(
        map(lambda car: car['price'] * 0.9 if car.get('mileage', 0) > 50000 else car['price'], car_data))
    return jsonify({"result": discounted_prices})


# Endpunkt /B3E
@app_instance.route('/B3E', methods=['GET'])
def b3e():
    car_data = [{'color': 'black', 'price': 8000}, {'color': 'blue', 'price': 12000},
                {'color': 'black', 'price': 10000}]
    # Lambda für die Sortierung von Autos nach Kilometerstand
    sorted_cars_by_mileage = sorted(car_data, key=lambda car: car.get('mileage', 0))

    # Lambda für die Sortierung von Autos nach Preis in absteigender Reihenfolge
    sorted_cars_by_price_desc = sorted(car_data, key=lambda car: car['price'], reverse=True)
    return jsonify({"result_sorted_by_mileage": sorted_cars_by_mileage,
                    "result_sorted_by_price_desc": sorted_cars_by_price_desc})


@app_instance.route('/B4G', methods=['GET'])
def b4g():
    # Map: Aktualisierung aller Autopreise um 10%
    car_prices = [5000, 8000, 12000, 15000]
    updated_prices = list(map(lambda price: price * 1.1, car_prices))

    # Filter: Auswahl nur von Autos mit Preis über 10000
    expensive_cars = list(filter(lambda price: price > 10000, car_prices))

    # Reduce: Berechnung des Gesamtpreises aller Autos
    from functools import reduce
    total_price = reduce(lambda x, y: x + y, car_prices)
    return jsonify({"result_updated_prices": updated_prices,
                    "result_expensive_cars": expensive_cars,
                    "result_total_price": total_price})


@app_instance.route('/B4F', methods=['GET'])
def b4f():
    # Kombination von Map und Filter: Rabatt von 5% auf alle schwarzen Autos
    car_data = [{'color': 'black', 'price': 8000}, {'color': 'blue', 'price': 12000},
                {'color': 'black', 'price': 10000}]
    discounted_black_cars = list(
        map(lambda car: car['price'] * 0.95, filter(lambda car: car['color'] == 'black', car_data)))

    # Kombination von Filter und Reduce: Gesamtpreis aller blauen Autos
    total_price_blue_cars = reduce(lambda x, y: x + y['price'], filter(lambda car: car['color'] == 'blue', car_data), 0)
    return jsonify({"result_discounted_black_cars": discounted_black_cars,
                    "result_total_price_blue_cars": total_price_blue_cars})


@app_instance.route('/B4E', methods=['GET'])
def b4e():
    car_data = [{'color': 'black', 'price': 8000}, {'color': 'blue', 'price': 12000},
                {'color': 'black', 'price': 10000}]
    # Verwendung von Map zur Berechnung des Gesamtpreises mit Steuern
    tax_rate = 0.1
    total_price_with_tax = list(map(lambda car: car['price'] * (1 + tax_rate), car_data))

    # Verwendung von Reduce zur Aggregation von Rabatten auf schwarze Autos
    discount_on_black_cars = reduce(lambda acc, car: acc + (car['price'] * 0.05),
                                    filter(lambda car: car['color'] == 'black', car_data), 0)
    return jsonify(
        {"result_total_price_with_tax": total_price_with_tax, "discount_on_black_cars": discount_on_black_cars})


if __name__ == '__main__':
    # Starte die Flask-Anwendung
    app_instance.run(debug=True)
