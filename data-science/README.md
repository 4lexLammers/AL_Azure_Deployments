# Data Science Workspace

This directory contains data science notebooks, experiments, and related artifacts.

## Structure

```
data-science/
├── notebooks/           # Jupyter notebooks for analysis
├── data/               # Data files
│   ├── raw/           # Original, immutable data
│   ├── interim/       # Intermediate data transformations
│   ├── processed/     # Final, canonical datasets
│   └── external/      # Data from third-party sources
├── models/            # Trained models and model artifacts
├── reports/           # Generated analysis reports
│   └── figures/       # Visualizations and charts
└── references/        # Documentation, manuals, and references
```

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r ../requirements.txt  # Use root requirements for data science packages
   ```

3. Start Jupyter:
   ```bash
   jupyter lab notebooks/
   ```

## Data Management

- **Raw Data**: Store original data in `data/raw/` - never modify these files
- **Processed Data**: Store cleaned, transformed data in `data/processed/`
- **Interim Data**: Use `data/interim/` for intermediate processing steps
- **External Data**: Store third-party data in `data/external/`

## Model Management

- Save trained models in `models/` with descriptive names
- Include model metadata and performance metrics
- Version your models appropriately

## Notebooks

- Use descriptive names for notebooks
- Number notebooks in order of execution if they form a pipeline
- Document your analysis clearly with markdown cells

## Integration with Azure Functions

This data science workspace is separate from the Azure Functions application but can:
- Export models for use in functions
- Generate processed datasets for function endpoints
- Prototype functionality before implementing in production functions
