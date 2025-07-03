# Infrastructure as Code

This directory contains Bicep templates for provisioning Azure resources.

## Structure

```
infra/
├── main.bicep                 # Main infrastructure template
├── main.parameters.json       # Parameters for deployment
└── modules/                   # Reusable Bicep modules (if any)
```

## Resources Deployed

- **Azure Functions App**: Serverless compute for the application
- **Storage Account**: Function app storage and data persistence
- **Application Insights**: Monitoring and logging
- **Log Analytics Workspace**: Centralized logging
- **Key Vault**: Secure secrets management
- **App Service Plan**: Consumption plan for Functions
- **User-Assigned Managed Identity**: Secure authentication

## Security Features

- **Managed Identity**: Eliminates need for stored credentials
- **RBAC**: Proper role assignments for least privilege access
- **HTTPS Only**: All traffic encrypted in transit
- **Key Vault Integration**: Secure secrets storage
- **Network Security**: Configured with appropriate access controls

## Deployment

The infrastructure is deployed automatically via Azure Developer CLI:

```bash
azd up
```

## Customization

Modify parameters in `main.parameters.json` or environment variables to customize the deployment:

- `environmentName`: Prefix for resource names
- `location`: Azure region for deployment

## Monitoring

- **Application Insights**: Performance and usage monitoring
- **Log Analytics**: Centralized logging and querying
- **Diagnostic Settings**: Comprehensive telemetry collection
