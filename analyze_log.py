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


LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) - (?P<country>\S+) - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) (?P<httpver>\S+)" '
    r'(?P<status>\d+) (?P<bytes>\d+) "-" "(?P<useragent>[^"]+)" (?P<responsetime>\d+)$'
)
# This regular expression matches each log line and extracts fields like IP, country, timestamp, HTTP method, path, status, bytes, user agent, and response time.

def parse_log_line(line):
    """
    Parse a single log line using the LOG_PATTERN regex.
    Returns a dictionary of extracted fields if the line matches, else None.
    """
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_log(log_path):
    """
    Analyze the log file at log_path and print statistics about IPs, user agents, and paths.
    Also flags potential bots/high-frequency IPs.
    """

    # Initialize counters and mappings to store analysis results
    ip_counter = Counter()
    useragent_counter = Counter()
    path_counter = Counter()
    ip_to_useragents = defaultdict(set)
    ip_to_paths = defaultdict(set)

    # Open the log file for reading
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parsed = parse_log_line(line.strip())  # Parse each line
            if not parsed:
                continue  # Skip lines that don't match the expected format
            ip = parsed['ip']
            useragent = parsed['useragent']
            path = parsed['path']
            # Update counters and mappings
            ip_counter[ip] += 1
            useragent_counter[useragent] += 1
            path_counter[path] += 1
            ip_to_useragents[ip].add(useragent)
            ip_to_paths[ip].add(path)

    # Print top 10 IPs by request count, with user agent and path diversity
    print("\nTop 10 IPs by request count:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} requests, {len(ip_to_useragents[ip])} user agents, {len(ip_to_paths[ip])} unique paths")

    # Print top 10 user agents by request count
    print("\nTop 10 User Agents:")
    for ua, count in useragent_counter.most_common(10):
        print(f"{ua[:80]}...: {count} requests")

    # Print top 10 requested paths
    print("\nTop 10 Requested Paths:")
    for path, count in path_counter.most_common(10):
        print(f"{path}: {count} requests")

    # Print IPs with more than 100 requests (potential bots/high-frequency)
    print("\nPotential bot/high-frequency IPs (over 100 requests):")
    for ip, count in ip_counter.items():
        if count > 100:
            print(f"{ip}: {count} requests, {len(ip_to_useragents[ip])} user agents, {len(ip_to_paths[ip])} unique paths")

def main():
    """
    Entry point for the script. Checks command-line arguments and runs analysis.
    """
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <logfile>")
        sys.exit(1)
    analyze_log(sys.argv[1])

# Run main() if this script is executed directly
if __name__ == "__main__":
    main()