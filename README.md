
# Log Analysis for Music Media Startup

This project analyzes web server logs to identify suspicious (potentially non-human) traffic and high-frequency IPs that may be overwhelming your servers.

## Requirements
- Python 3.8 or newer
- No external Python packages required

## Usage

1. Place your log file (e.g., `sample-log.log`) in this directory.
2. Open a terminal (PowerShell or Command Prompt) in this directory.
3. Run the analysis script:

```powershell
python analyze_log.py sample-log.log
```

The script will output:
- Top 10 IPs by request count
- Top 10 user agents
- Top 10 requested paths
- List of IPs with more than 100 requests (potential bots)

## (Optional) Run with Docker

1. Build the Docker image:
   ```powershell
   docker build -t log-analyzer .
   ```
2. Run the analysis (mount your log file):
   
   **Important:** On Windows, `$PWD` may not work for volume mounting. Use your folder's full path instead. For example:
   ```powershell
   docker run --rm -v "C:\Users\Raghav Commandur\Downloads\ieuk-task-2025-main\ieuk-task-2025-main:/app" log-analyzer sample-log.log
   ```
   Replace the path above with your own folder location. The example uses the path for this project; yours may be different.

## Troubleshooting
- If you see `Python was not found`, install Python from [python.org](https://www.python.org/downloads/) and ensure it is added to your PATH.
- For Docker, make sure Docker Desktop is running and you are in the correct folder.

## Interpretation
- IPs with extremely high request counts, especially with few user agents or paths, are likely bots or scrapers.
- Consider rate-limiting or blocking these IPs, or using a CAPTCHA for suspicious traffic.
- Use a CDN or web application firewall for additional protection.
