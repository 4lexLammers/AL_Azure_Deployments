# Azure Function App

This directory contains the Azure Functions application using the Python v2 programming model.

## Structure

```
function_app/
├── function_app.py        # Main function app with HTTP trigger
├── requirements.txt       # Python dependencies
├── host.json             # Function host configuration
├── local.settings.json   # Local development settings
├── .funcignore          # Files to ignore during deployment
└── .gitignore           # Git ignore patterns
```

## Features

- **Python v2 Programming Model**: Uses the latest Azure Functions programming model
- **HTTP Trigger**: RESTful API endpoint
- **JSON Response**: Returns structured data in JSON format
- **Error Handling**: Comprehensive error handling and logging
- **CORS Enabled**: Cross-origin requests supported

## Local Development

1. Install Azure Functions Core Tools
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the function locally:
   ```bash
   func start
   ```

## API Endpoints

### GET/POST `/api/function`

Returns test data with optional name parameter.

**Query Parameters:**
- `name` (optional): Personalized greeting

**Request Body (POST):**
```json
{
  "name": "TestUser"
}
```

**Response:**
```json
{
  "message": "Function executed successfully!",
  "data": [
    {"id": 1, "value": 42.5, "category": "A"},
    {"id": 2, "value": 38.2, "category": "B"}
  ],
  "rows": 5,
  "status": "success"
}
```

## Authentication

The function uses Function-level authentication. Include the function key in requests:
- Query parameter: `?code=<function-key>`
- Header: `x-functions-key: <function-key>`

## Deployment

Deploy using Azure Developer CLI:
```bash
azd up
```
