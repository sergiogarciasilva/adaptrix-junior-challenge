# Environment Setup

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- An LLM API key (OpenAI, Anthropic, or similar)

## Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the project root:

```bash
# For OpenAI
OPENAI_API_KEY=your-api-key-here

# For Anthropic
ANTHROPIC_API_KEY=your-api-key-here
```

Or set as environment variable:

```bash
export OPENAI_API_KEY=your-api-key-here
```

## Running the Solution

```bash
cd src
python extract_entities.py
```

## Running Tests

```bash
pytest tests/
```

## Troubleshooting

### ModuleNotFoundError
Ensure you're in the virtual environment and have run `pip install -r requirements.txt`

### API Key Errors
Verify your API key is set correctly in `.env` or as an environment variable

### DOCX Reading Errors
Check that the input file exists at `input/gearhead_weekly_report.docx`
