import random
from validation import validate_measurement


def generate_measurement():
    voltage = round(random.uniform(10.0, 13.5), 2)
    current = round(random.uniform(1.0, 7.0), 2)
    temperature = round(random.uniform(25.0, 100.0), 2)
    resistance = round(random.uniform(85.0, 115.0), 2)
    frequency = round(random.uniform(58.0, 62.0), 2)

    return {
        "voltage": voltage,
        "current": current,
        "temperature": temperature,
        "resistance": resistance,
        "frequency": frequency
    }


if __name__ == "__main__":
    measurement = generate_measurement()
    result, fault = validate_measurement(measurement)

    print("Measurement:")
    print(measurement)
    print()
    print("Result:", result)
    print("Fault:", fault)