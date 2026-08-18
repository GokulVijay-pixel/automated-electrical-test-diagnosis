import pandas as pd
import matplotlib.pyplot as plt
from database import create_connection


def load_data():
    connection = create_connection()

    query = """
        SELECT
            measurement_id,
            test_time,
            voltage,
            current,
            temperature,
            resistance,
            frequency,
            result,
            fault
        FROM test_measurements
    """

    dataframe = pd.read_sql(query, connection)

    connection.close()

    return dataframe


def analyze_data():
    df = load_data()

    print("\n========== TEST DATA ANALYSIS ==========")

    print(f"Total tests: {len(df)}")

    pass_count = (df["result"] == "PASS").sum()
    fail_count = (df["result"] == "FAIL").sum()

    print(f"Passed tests: {pass_count}")
    print(f"Failed tests: {fail_count}")

    if len(df) > 0:
        failure_rate = fail_count / len(df) * 100
        print(f"Failure rate: {failure_rate:.2f}%")

    print("\nAverage measurements:")

    print(f"Voltage:     {df['voltage'].mean():.2f} V")
    print(f"Current:     {df['current'].mean():.2f} A")
    print(f"Temperature: {df['temperature'].mean():.2f} °C")
    print(f"Resistance:  {df['resistance'].mean():.2f} Ohm")
    print(f"Frequency:   {df['frequency'].mean():.2f} Hz")

def plot_temperature():
    df = load_data()

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["measurement_id"],
        df["temperature"],
        marker="o"
    )

    plt.axhline(85, linestyle="--", label="Maximum specification")
    plt.axhline(-20, linestyle="--", label="Minimum specification")

    plt.title("Temperature Across Electrical Tests")
    plt.xlabel("Test Number")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("temperature_test_results.png")

    print("Temperature graph saved.")

def plot_voltage_current():
    df = load_data()

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["measurement_id"],
        df["voltage"],
        marker="o",
        label="Voltage (V)"
    )

    plt.plot(
        df["measurement_id"],
        df["current"],
        marker="x",
        label="Current (A)"
    )

    plt.title("Voltage and Current Across Tests")
    plt.xlabel("Test Number")
    plt.ylabel("Measurement")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("voltage_current_results.png")

    print("Voltage/current graph saved.")

def export_csv():
    df = load_data()

    df.to_csv("test_results.csv", index=False)

    print("Test data exported to test_results.csv")

if __name__ == "__main__":
    analyze_data()
    plot_temperature()
    plot_voltage_current()
    export_csv()