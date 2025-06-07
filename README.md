# 🛡️ CodeGuard

## 📌 Project Overview

**CodeGuard** is a code analysis server that receives the latest version of a Python project (zipped), analyzes it, and returns feedback and graphs on code quality.

The project is designed to integrate with a simplified Git-like system called **WIT**.  
Once a `WIT PUSH` command is triggered, the zipped code is sent to this server for automatic analysis.

---

## ⚙️ Installation & Execution Instructions

### 🔧 Requirements

- Python 3.10+
- pip (Python package manager)

### 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/CodeGuard.git
   cd CodeGuard
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Run the Server
Start the FastAPI server with:

bash
Copy
Edit
uvicorn main:app --reload
Once running, the server is accessible at:
http://127.0.0.1:8000

📁 Folder Structure
bash
Copy
Edit
CodeGuard/
│
├── main.py                 # FastAPI application
├── Graph.py                # Responsible for graph generation
├── CodeAnalysis.py         # Static analysis logic
├── requirements.txt        # Project dependencies
├── README.md               # Documentation file
└── Graphs/                 # Output folder for generated graphs
📡 API Endpoints
Method	Endpoint	Description
POST	/analyze	Accepts a .zip file containing .py files and returns paths to generated analysis graphs.

📥 /analyze
Method: POST

Request Body: multipart/form-data with a .zip file under field file

Response: JSON list of file paths to graphs

✅ Example:
bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/analyze \
  -F "file=@my_project.zip"
📊 Output
After analyzing your uploaded Python project, the server generates:

📊 Histogram per file — function lengths

🥧 Pie chart — error types distribution

📉 Bar chart — errors per file

Saved in the Graphs/ directory with .png format.

🧪 Checks Performed
The system detects:

Check	Description
File too long	File exceeds 200 lines
Function too long	Function exceeds 20 lines
Function missing docstring	No documentation string in function
Unused variable	Variable defined but never used

👤 Author
Developed as part of an advanced Python course
Includes integration with a custom version control project named WIT (similar to Git).
