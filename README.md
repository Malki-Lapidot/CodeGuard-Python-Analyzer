# 🛡️ CodeGuard - Code Analysis System

## 📋 Project Overview

**CodeGuard** is an advanced code analysis system that integrates with the `wit push` command to ensure high-quality code is maintained across all commits. The system performs automatic analysis of Python files, detects common code quality issues, and provides visual insights through graphs.

### 🎯 Project Goal
Develop a backend system that automatically analyzes Python files every time the user runs `wit push`, detects code quality issues, and returns visual graphs with insights.

---

## 🧰 Technologies

- **Language**: Python
- **Server**: FastAPI  
- **Code Analysis**: ast (Abstract Syntax Tree)
- **Visualization**: matplotlib
- **Version Control**: wit (custom system)

---

## 🏗️ Project Structure

```
CodeGuard/
├── README.md
├── requirements.txt
├── main.py                 # Main FastAPI server
├── wit/
│   ├── __init__.py
│   ├── wit.py             # Version control system
│   └── commands.py        # wit commands (init, add, commit, log, push)
├── analyzer/
│   ├── __init__.py
│   ├── code_analyzer.py   # Code analysis using AST
│   └── quality_checks.py  # Code quality checks
├── visualization/
│   ├── __init__.py
│   └── graph_generator.py # Graph generation
├── static/
│   └── graphs/           # Generated graphs directory
└── tests/
    ├── __init__.py
    └── test_analyzer.py   # Unit tests
```

---

## 🚀 Installation and Setup

### Prerequisites
- Python 3.8+
- pip

### Installation Steps

1. **Clone the project**
   ```bash
   git clone https://github.com/HadassaAvimorNew/CodeGuard.git
   cd CodeGuard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Initialize wit system**
   ```bash
   python -m wit init
   ```

---

## 🌐 API Endpoints

### POST `/analyze`
**Description**: Accepts files and returns visual graphs

**Request Example**:
```json
{
  "files": [
    {
      "name": "example.py",
      "content": "def hello():\n    print('Hello World')"
    }
  ]
}
```

**Response Example**:
```json
{
  "graphs": {
    "function_length_histogram": "/static/graphs/func_length_hist.png",
    "issues_pie_chart": "/static/graphs/issues_pie.png",
    "issues_per_file_bar": "/static/graphs/issues_bar.png"
  },
  "analysis_summary": {
    "total_files": 1,
    "total_functions": 1,
    "total_issues": 2
  }
}
```

### POST `/alerts`
**Description**: Accepts files and returns issue warnings

**Request Example**:
```json
{
  "files": [
    {
      "name": "example.py", 
      "content": "def long_function():\n    # 25 lines of code..."
    }
  ]
}
```

**Response Example**:
```json
{
  "alerts": [
    {
      "file": "example.py",
      "line": 1,
      "type": "function_length",
      "message": "Function 'long_function' is too long (25 lines, recommended < 20)",
      "severity": "warning"
    }
  ]
}
```

---

## 🔍 Code Quality Checks

The system performs the following checks using AST:

| Check Type | Description | Warning Threshold |
|------------|-------------|------------------|
| **Function Length** | Detect functions that are too long | >20 lines |
| **File Length** | Detect files that are too long | >200 lines |
| **Unused Variables** | Detect variables that are assigned but never used | - |
| **Missing Docstrings** | Detect functions without documentation strings | - |
| **🌟 Bonus**: Non-English Variables | Detect variables written in non-English letters | - |

---

## 📊 Visual Graphs

The system generates the following graphs using matplotlib:

1. **Histogram** - Distribution of function lengths
2. **Pie Chart** - Number of issues per issue type  
3. **Bar Chart** - Number of issues per file
4. **🌟 Bonus**: Line graph to track the number of issues over time

All graphs are saved as PNG files and accessible through static paths.

---

## 🎮 Using the wit System

### Available Commands

```bash
# Initialize new repository
python -m wit init

# Add files to tracking
python -m wit add 

# Create commit
python -m wit commit -m "commit message"

# Show commit history
python -m wit log

# Push to server and analyze code
python -m wit push
```

### Example Workflow

```bash
# Initialize project
python -m wit init

# Add Python file
echo "def hello(): print('world')" > example.py
python -m wit add example.py

# Create commit
python -m wit commit -m "Add hello function"

# Push and analyze
python -m wit push
```

---

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_analyzer.py -v

# Check code coverage
python -m pytest --cov=analyzer tests/
```

---

## 🔧 Configuration and Customization

### Configuration File (config.py)
```python
# Code analysis settings
MAX_FUNCTION_LENGTH = 20
MAX_FILE_LENGTH = 200
GENERATE_TIME_SERIES = True

# Server settings
HOST = "0.0.0.0" 
PORT = 8000
DEBUG = True

# File paths
GRAPHS_DIR = "static/graphs"
TEMP_DIR = "temp"
```

---

## 📈 Usage Examples

### Analyzing a Single File
```python
import requests

files_data = {
    "files": [
        {
            "name": "my_script.py",
            "content": open("my_script.py").read()
        }
    ]
}

response = requests.post("http://localhost:8000/analyze", json=files_data)
graphs = response.json()["graphs"]
print(f"Graphs generated: {list(graphs.keys())}")
```

### Getting Alerts
```python
response = requests.post("http://localhost:8000/alerts", json=files_data)
alerts = response.json()["alerts"]
for alert in alerts:
    print(f"⚠️ {alert['message']}")
```

---

## 🤝 Contributing

1. Fork the project
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is submitted as part of the Backend Development final project.

---

## 📞 Contact

**Developer**: HadassaAvimorNew  
**GitHub**: [HadassaAvimorNew](https://github.com/HadassaAvimorNew)

---

## 🏆 Advanced Features (Bonus)

- ✅ Detection of non-English variable names  
- ✅ Line graph for tracking issues over time
- ✅ Advanced alert system
- ✅ Complete and documented API
- ✅ Comprehensive unit tests

---

## 🚀 Features Implemented

### Core Features
- ✅ FastAPI server with two endpoints
- ✅ AST-based code analysis
- ✅ Function length validation (>20 lines)
- ✅ File length validation (>200 lines)
- ✅ Unused variable detection
- ✅ Missing docstring detection
- ✅ Visual graph generation with matplotlib

### Visualization
- ✅ Function length histogram
- ✅ Issues distribution pie chart
- ✅ Issues per file bar chart
- ✅ Time series analysis (bonus)

### wit Version Control System
- ✅ `wit init` - Initialize repository
- ✅ `wit add` - Add files to tracking
- ✅ `wit commit` - Create commits
- ✅ `wit log` - Show commit history
- ✅ `wit push` - Push and trigger analysis

### Quality Assurance
- ✅ Comprehensive error handling
- ✅ Input validation
- ✅ Unit tests coverage
- ✅ Clean code structure
- ✅ Detailed documentation

---

*Built with ❤️ for CodeGuard - Advanced Code Analysis System*
