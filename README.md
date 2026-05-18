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
```

ngrok public URL examples:

```text
https://upfront-snort-concur.ngrok-free.dev/
https://upfront-snort-concur.ngrok-free.dev/api/foods
https://upfront-snort-concur.ngrok-free.dev/api/foods/FS-001
```


## Video Tutorial

Video tutorial link: [Watch the video tutorial](https://drive.google.com/file/d/1AKNvAihTtx5HxQbUyC1lJ3QX05yKAZlf/view?usp=sharing)


