# Azure Functions Data Application

A modern Azure Functions application with integrated data science workspace, built using Azure Developer CLI and following Microsoft's best practices.

## 🏗️ Architecture

This repository contains:
- **Azure Functions App** (Python v2 programming model)
- **Infrastructure as Code** (Bicep templates)
- **Data Science Workspace** (Jupyter notebooks and experiments)
- **CI/CD Pipeline** (GitHub Actions via AZD)

## 📁 Repository Structure

```
AL_Azure_Deployments/
├── function_app/              # Azure Functions application (v2 model)
│   ├── function_app.py        # Main function app with HTTP trigger
│   ├── requirements.txt       # Function dependencies
│   ├── host.json             # Function host configuration
│   ├── local.settings.json   # Local development settings
│   └── README.md             # Function app documentation
├── infra/                    # Infrastructure as Code (Bicep)
│   ├── main.bicep            # Main infrastructure template
│   └── README.md             # Infrastructure documentation
├── data-science/            # Data science workspace
│   ├── notebooks/           # Jupyter notebooks
│   ├── data/               # Datasets (raw, processed, interim, external)
│   ├── models/             # ML models and artifacts
│   ├── reports/            # Analysis reports and visualizations
│   └── README.md           # Data science documentation
├── .azure/                 # AZD configuration and state
├── azure.yaml              # Azure Developer CLI configuration
├── .gitignore              # Git ignore patterns
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Developer CLI](https://docs.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd)
- [Python 3.11+](https://www.python.org/downloads/)
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)

### Deploy to Azure

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AL_Azure_Deployments
   ```

2. **Login to Azure**
   ```bash
   azd auth login
   ```

3. **Deploy infrastructure and application**
   ```bash
   azd up
   ```

This will:
- Provision Azure resources (Functions App, Storage, Application Insights, etc.)
- Deploy the function application
- Set up monitoring and logging

### Local Development

1. **Navigate to function app directory**
   ```bash
   cd function_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start local development server**
   ```bash
   func start
   ```

4. **Test the function**
   ```bash
   curl "http://localhost:7071/api/function?name=LocalTest"
   ```

## 📊 Data Science Workflow

1. **Set up data science environment**
   ```bash
   cd data-science
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r ../requirements.txt
   ```

2. **Start Jupyter Lab**
   ```bash
   jupyter lab notebooks/
   ```

3. **Organize your work**
   - Place raw data in `data/raw/`
   - Save processed datasets in `data/processed/`
   - Store models in `models/`
   - Generate reports in `reports/`

## 🔧 API Endpoints

### HTTP Trigger Function

**Endpoint**: `GET/POST /api/function`

**Parameters**:
- `name` (optional): Personalized greeting

**Example Response**:
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

## 🔐 Security

- **Managed Identity**: No stored credentials required
- **Function-level Authentication**: Secure API access
- **HTTPS Only**: All communication encrypted
- **Key Vault Integration**: Secure secrets management
- **RBAC**: Least privilege access controls

## 📈 Monitoring

- **Application Insights**: Performance monitoring and telemetry
- **Log Analytics**: Centralized logging and querying
- **Custom Metrics**: Business-specific monitoring
- **Alerts**: Proactive issue detection

## 🔄 CI/CD

The repository includes GitHub Actions workflows for:
- Automated testing
- Infrastructure deployment
- Application deployment
- Security scanning

## 🛠️ Technology Stack

- **Azure Functions**: Serverless compute platform
- **Python 3.11**: Runtime environment
- **Bicep**: Infrastructure as Code
- **Azure Developer CLI**: Deployment orchestration
- **Application Insights**: Monitoring and logging
- **Managed Identity**: Secure authentication
- **GitHub Actions**: CI/CD pipeline

## 📚 Documentation

- [Function App Documentation](./function_app/README.md)
- [Infrastructure Documentation](./infra/README.md)
- [Data Science Documentation](./data-science/README.md)
- [Azure Functions Python Developer Guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `func start`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
