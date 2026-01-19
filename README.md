# Calculator Project

## Project Structure

```
.
├── poc1/              # First proof of concept
│   ├── calculator.py
│   └── requirements.txt
├── venv/              # Virtual environment
├── .gitignore
└── README.md
```

## Setup

1. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r poc1/requirements.txt
```

3. Run the calculator:
```bash
python poc1/calculator.py
```
