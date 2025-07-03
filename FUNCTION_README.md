# Azure Function App - Data Generator

This is an Azure Function App v1 that generates random data using pandas and returns it as JSON.

## Function Details

- **Type**: HTTP Trigger
- **Programming Model**: Azure Functions v1 (Python)
- **Runtime**: Python 3.9+
- **Authorization Level**: Function (requires function key)

## API Endpoints

### GET/POST `/api/function`

Generates a random DataFrame with 3 columns (A, B, C) and 10 rows.

**Query Parameters:**
- `name` (optional): Your name to personalize the response

**Example Requests:**
```bash
# Simple request
curl https://your-function-app.azurewebsites.net/api/function?code=YOUR_FUNCTION_KEY

# With name parameter
curl https://your-function-app.azurewebsites.net/api/function?name=Alex&code=YOUR_FUNCTION_KEY

# POST with JSON body
curl -X POST https://your-function-app.azurewebsites.net/api/function?code=YOUR_FUNCTION_KEY \
  -H "Content-Type: application/json" \
  -d '{"name": "Alex"}'
```

**Response Format:**
```json
{
  "message": "Hello Alex! Here's your random data:",
  "data": [
    {"A": 0.123, "B": 0.456, "C": 0.789},
    ...
  ],
  "rows": 10,
  "columns": ["A", "B", "C"]
}
```

## Local Development

1. Install Azure Functions Core Tools:
   ```bash
   npm install -g azure-functions-core-tools@4 --unsafe-perm true
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the function locally:
   ```bash
   func start
   ```

4. Test locally:
   ```bash
   curl http://localhost:7071/api/function
   ```

## Deployment to Azure

### Prerequisites
- Azure CLI installed
- Azure subscription
- Function App created in Azure

### Deploy using Azure CLI

1. Login to Azure:
   ```bash
   az login
   ```

2. Create a resource group (if needed):
   ```bash
   az group create --name myResourceGroup --location eastus
   ```

3. Create a storage account:
   ```bash
   az storage account create --name mystorageaccount --location eastus --resource-group myResourceGroup --sku Standard_LRS
   ```

4. Create the Function App:
   ```bash
   az functionapp create \
     --resource-group myResourceGroup \
     --consumption-plan-location eastus \
     --runtime python \
     --runtime-version 3.9 \
     --functions-version 4 \
     --name myFunctionApp \
     --storage-account mystorageaccount
   ```

5. Deploy the function:
   ```bash
   func azure functionapp publish myFunctionApp
   ```

### Deploy using VS Code

1. Install the Azure Functions extension
2. Sign in to Azure
3. Right-click on the function and select "Deploy to Function App"
4. Follow the prompts to create or select a Function App

## Configuration

- **Function timeout**: 5 minutes (configurable in host.json)
- **Extension bundle**: Latest v4 bundle for bindings
- **Logging**: Application Insights enabled with sampling

## Security Considerations

- Function uses "function" authorization level (requires function key)
- CORS is enabled for all origins (modify for production)
- No sensitive data is logged
- Input validation and error handling implemented

## Monitoring

The function includes comprehensive logging for:
- Request processing
- Successful DataFrame generation
- Error handling and debugging

View logs in Azure Portal > Function App > Monitor or use Application Insights for detailed telemetry.
