import sys  # For command-line argument handling and exiting
import re   # For regular expression parsing of log lines
from collections import Counter, defaultdict  # For counting and grouping data


# Sample log from the original file:
# 100.34.17.233 - NO - [01/07/2025:06:00:02] "GET /news/grammy-nominations-2024 HTTP/1.1" 302 1234 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" 269
# 173.80.18.254 - NO - [01/07/2025:06:00:04] "POST / HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" 124
# 10.3.0.48 - SE - [01/07/2025:06:00:06] "GET /podcasts/behind-the-beat HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1" 284
#
# How the log format was deduced:
# By examining the sample lines, we see each log entry contains:
#   - An IP address (e.g., 100.34.17.233)
#   - A country code (e.g., NO)
#   - A timestamp in square brackets (e.g., [01/07/2025:06:00:02])
#   - An HTTP request in quotes (e.g., "GET /news/grammy-nominations-2024 HTTP/1.1")
#   - A status code (e.g., 302)
#   - A byte count (e.g., 1234)
#   - A dash ("-")
#   - A user agent string in quotes
#   - A response time (e.g., 269)
# Each part is separated by spaces or quotes, which informed the construction of the regular expression (LOG_PATTERN) to extract these fields for analysis.
