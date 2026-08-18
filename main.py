from sensor_simulator import generate_measurement
from validation import validate_measurement
from database import save_measurement


def run_test():
    measurement = generate_measurement()

    result, fault = validate_measurement(measurement)

    print("\n========== ELECTRICAL TEST ==========")
    print(f"Voltage:      {measurement['voltage']} V")
    print(f"Current:      {measurement['current']} A")
    print(f"Temperature:  {measurement['temperature']} °C")
    print(f"Resistance:   {measurement['resistance']} Ohm")
    print(f"Frequency:    {measurement['frequency']} Hz")
    print("-------------------------------------")
    print(f"RESULT:       {result}")
    print(f"FAULT:        {fault}")
    print("=====================================")

    save_measurement(measurement, result, fault)


if __name__ == "__main__":
    run_test()

def run_multiple_tests(number_of_tests):
    for i in range(number_of_tests):
        print(f"\nRunning test {i + 1}/{number_of_tests}...")
        run_test()


if __name__ == "__main__":
    run_multiple_tests(50)