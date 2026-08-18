# Automated Electrical Test & Fault Diagnosis System

## Overview

This project is a Python-based automated electrical test system designed to simulate an engineering test-bench workflow.

The system generates electrical measurements, validates them against configurable engineering specifications, automatically determines PASS/FAIL status, identifies potential faults, stores test results in MySQL, and performs statistical analysis and visualization.

## Problem

Electrical and electronic hardware testing can generate large volumes of measurements. Manually reviewing measurements against specifications is repetitive and can make it difficult to identify failure trends.

This project demonstrates how software can automate the measurement validation and analysis process.

## System Workflow

Sensor/Test Data
        ↓
Python Test Simulator
        ↓
Engineering Specification Validation
        ↓
PASS / FAIL
        ↓
Fault Diagnosis
        ↓
MySQL Database
        ↓
SQL + Pandas Analysis
        ↓
Engineering Visualizations

## Features

- Simulated electrical test measurements
- Voltage, current, temperature, resistance, and frequency monitoring
- Automated engineering specification checking
- PASS/FAIL classification
- Rule-based fault diagnosis
- MySQL test-result storage
- SQL-based statistical analysis
- Pandas data analysis
- Matplotlib engineering visualizations
- CSV data export

## Technologies

- Python
- MySQL
- SQL
- Pandas
- Matplotlib
- Git/GitHub

## Engineering Specifications

| Parameter | Acceptable Range |
|---|---|
| Voltage | 11.5–12.5 V |
| Current | 0–5 A |
| Temperature | -20–85 °C |
| Resistance | 90–110 Ω |
| Frequency | 59–61 Hz |

## Example Output

The system reports measurements and automatically identifies failures such as:

- Overcurrent
- Overtemperature
- Voltage out of specification
- Resistance out of specification
- Frequency out of specification

## Future Improvements

Potential future development includes:

- Real hardware/DAQ integration
- Serial communication
- CAN-based automotive test data
- Automated test sequencing
- Statistical process control
- More advanced fault classification
- Automated PDF test reports
- Web-based engineering dashboard