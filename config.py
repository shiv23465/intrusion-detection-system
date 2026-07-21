import os

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
SIGNATURE_DIR = os.path.join(BASE_DIR, "signatures")

# Files
LOG_FILE = os.path.join(LOG_DIR, "ids.log")
JSON_REPORT = os.path.join(REPORT_DIR, "report.json")
HTML_REPORT = os.path.join(REPORT_DIR, "report.html")

# Monitoring

MONITOR_FOLDER = os.path.join(BASE_DIR, "monitor")

CHECK_INTERVAL = 5

MAX_FAILED_CONNECTIONS = 15

# Network

PACKET_LIMIT = 500

# Create folders automatically

for folder in [LOG_DIR, REPORT_DIR, SIGNATURE_DIR, MONITOR_FOLDER]:
    os.makedirs(folder, exist_ok=True)
