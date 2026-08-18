
def validate_measurement(measurement):
    faults = []

    if not 11.5 <= measurement["voltage"] <= 12.5:
        faults.append("Voltage out of specification")

    if not 0 <= measurement["current"] <= 5.0:
        faults.append("Overcurrent")

    if not -20 <= measurement["temperature"] <= 85:
        faults.append("Overtemperature")

    if not 90 <= measurement["resistance"] <= 110:
        faults.append("Resistance out of specification")

    if not 59 <= measurement["frequency"] <= 61:
        faults.append("Frequency out of specification")

    if faults:
        return "FAIL", "; ".join(faults)

    return "PASS", "None"
