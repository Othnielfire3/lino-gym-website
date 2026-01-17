# for windows 
python -m venv .venv

# to load up localhost
cd back-end
python app.py 

# to restore all data including flask
pip install -r requirements.txt

# to install new virtual environment
PowerShell: .\.venv\Scripts\Activate.ps1
Command Prompt: .\.venv\Scripts\activate.bat