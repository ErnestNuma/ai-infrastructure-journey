# Log Intelligence Engine (v1.0)

Parses Debian system logs and exports structured JSON reports
for infrastructure monitoring and analysis.

## What it does
- Reads /var/log/syslog
- Counts total errors and warnings
- Calculates error rate as a percentage
- Extracts the 5 most recent error and warning lines
- Saves a structured log_report.json file

## How to run
sudo python3 log_intel.py

## Output format
log_report.json with sections:
- report_metadata (when, what file, how many lines)
- summary (error count, warning count, error rate %)
- recent_errors (last 5 error lines)
- recent_warnings (last 5 warning lines)

## Modules used
- json   — serialize Python dict to JSON file
- os     — build file paths dynamically
- datetime — timestamp the report
