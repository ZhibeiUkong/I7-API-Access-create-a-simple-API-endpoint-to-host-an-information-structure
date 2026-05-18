# I7-API-Access-create-a-simple-API-endpoint-to-host-an-information-structure
# Food Safety API

## Project Overview

This project creates a simple Flask API endpoint to host a food safety information structure. The information structure is based on our group project idea: a QR-code-based food safety system that allows users to check food origin, supplier, processing location, batch number, safety status, recall status, allergen information, and inspection agency information.

The goal of this API is to make the food safety data accessible through a simple GET request. This supports data portability because the information is stored in a structured JSON format and can be retrieved by other tools, browsers, or Python scripts.

## Information Structure

The main information structure is stored in:

```text
food_records.json
