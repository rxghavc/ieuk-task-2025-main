# Log Analysis for Music Media Startup

This project analyzes web server logs to identify suspicious (potentially non-human) traffic and high-frequency IPs that may be overwhelming your servers.

## Requirements
- Python 3.8 or newer
- No external Python packages required

## Usage

1. Place your log file (e.g., `sample-log.log`) in this directory.
2. Run the analysis script:

```sh
python analyze_log.py sample-log.log
```

The script will output:
- Top 10 IPs by request count
- Top 10 user agents
- Top 10 requested paths
- List of IPs with more than 100 requests (potential bots)

## (Optional) Run with Docker

1. Build the Docker image:
   ```sh
   docker build -t log-analyzer .
   ```
2. Run the analysis (mount your log file):
   ```sh
   docker run --rm -v $(pwd):/data log-analyzer python analyze_log.py /data/sample-log.log
   ```

---

**Interpretation:**
- IPs with extremely high request counts, especially with few user agents or paths, are likely bots or scrapers.
- Consider rate-limiting or blocking these IPs, or using a CAPTCHA for suspicious traffic.
