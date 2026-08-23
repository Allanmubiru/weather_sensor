# Weather_Pipeline

A small multi-file Python application for ingesting, validating, processing, and analysing local weather-sensor data.

## Project Structure

```
-weather_pipeline/
-gitignore
-main.py
-models.py
-processor.py
-README.md
```


## Features
- `Sensor` base class
- `TemperatureSensor` subclass using inheritance
- Temperature validation with `try` / `except`
- Generator-based record loading with `yield`
- List-comprehension filtering for temperatures above 30°C
- Multi-file integration through `main.py`
- Git-ready project with the virtual environment ignored

## Create and Activate the Virtual Environment

### Windows PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can allow scripts for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```
### Windows Command Prompt

```cmd
py -m venv venv
venv\Scripts\activate
```

## Run the Pipeline

From the project folder:

```powershell
py main.py
```

Expected output is similar to:
```
warning: invalid temperature value 'error' for sensor S2.

High temperatures:
[{'id': 3, 'temp': 31}]
```