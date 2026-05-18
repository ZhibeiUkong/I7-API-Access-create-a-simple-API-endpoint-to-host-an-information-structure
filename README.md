# Food Safety API

## Project Overview

This project creates a simple Flask API endpoint to host a food safety information structure. The information structure is based on our group project idea: a QR-code-based food safety system that allows users to check food origin, supplier, processing location, batch number, safety status, recall status, allergen information, and inspection agency information.

The goal of this API is to make food safety data accessible through simple GET requests. This supports data portability because the information is stored in a structured JSON format and can be retrieved by browsers, Python scripts, or other applications.

## Information Structure

The main information structure is stored in `food_records.json`.

Each food record includes the following fields: `product_id`, `product_name`, `category`, `origin_location`, `supplier`, `processing_location`, `batch_number`, `harvest_date`, `package_date`, `safety_status`, `recall_status`, `allergen_info`, `inspection_agency`, and `last_updated`.

These fields help users understand where a food product comes from, how it was processed, whether it has safety warnings, and which agency is responsible for inspection.

## Files in This Repository

This repository includes four main files: `food_records.json`, `food_api.py`, `test_api.py`, and `README.md`.

`food_records.json` stores the food safety information structure in JSON format. `food_api.py` runs the Flask API server and exposes the food safety records through API endpoints. `test_api.py` uses Python `requests.get()` to access the API through the ngrok public URL and print the response. `README.md` explains the project, API endpoints, setup process, testing process, and video tutorial link.

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Confirms that the API server is running |
| `/api/foods` | GET | Returns all food safety records |
| `/api/foods/<product_id>` | GET | Returns one food record by product ID |
| `/api/foods/search?status=Safe` | GET | Searches food records by safety status |
| `/api/foods/search?category=Vegetable` | GET | Searches food records by category |

## Example API Requests

Local Flask server examples:

```text
http://127.0.0.1:5002/
http://127.0.0.1:5002/api/foods
http://127.0.0.1:5002/api/foods/FS-001
http://127.0.0.1:5002/api/foods/search?status=Safe
```

ngrok public URL examples:

```text
https://upfront-snort-concur.ngrok-free.dev/
https://upfront-snort-concur.ngrok-free.dev/api/foods
https://upfront-snort-concur.ngrok-free.dev/api/foods/FS-001
https://upfront-snort-concur.ngrok-free.dev/api/foods/search?status=Safe
```

## How to Run the Flask Server Locally

Open Command Prompt and go to the project folder:

```bash
cd C:\Users\ROG\Downloads\myproject
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install Flask:

```bash
python -m pip install Flask
```

Run the Flask server on port 5002:

```bash
python -m flask --app food_api run -p 5002
```

If the server runs successfully, the terminal should show:

```text
Running on http://127.0.0.1:5002
```

## How to Expose the API with ngrok

Keep the Flask server running. Then open a second Command Prompt window and run:

```bash
ngrok http http://localhost:5002
```

ngrok will create a public forwarding URL, such as:

```text
https://upfront-snort-concur.ngrok-free.dev
```

This public URL can be used to access the local Flask API from outside the local machine.

## How to Test the API with Python Requests

Install the requests library:

```bash
python -m pip install requests
```

Run the test file:

```bash
python test_api.py
```

The script sends GET requests to the ngrok URL and prints the API responses.

Example code:

```python
import requests

base_url = "https://upfront-snort-concur.ngrok-free.dev"

print(requests.get(base_url + "/").text)

foods_response = requests.get(base_url + "/api/foods")
print(foods_response.json())

one_food_response = requests.get(base_url + "/api/foods/FS-001")
print(one_food_response.json())

search_response = requests.get(base_url + "/api/foods/search?status=Safe")
print(search_response.json())
```

## Video Tutorial

Video tutorial link: [Watch the video tutorial](https://drive.google.com/file/d/1AKNvAihTtx5HxQbUyC1lJ3QX05yKAZlf/view?usp=sharing)

## Notes

The Flask terminal must stay open while testing the API. The ngrok terminal must also stay open because the public URL only works while ngrok is running. If ngrok is restarted, the public URL may change, so the URL in `test_api.py` and this README may need to be updated.

This project satisfies the assignment requirements by selecting an information structure, hosting it through a Flask API endpoint, exposing the local endpoint with ngrok, and accessing the API through a Python `requests.get()` command.
