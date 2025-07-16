import unittest
from analyze_log import parse_log_line

class TestAnalyzeLog(unittest.TestCase):
    def test_parse_log_line_valid(self):
        line = '100.34.17.233 - NO - [01/07/2025:06:00:02] "GET /news/grammy-nominations-2024 HTTP/1.1" 302 1234 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" 269'
        result = parse_log_line(line)
        self.assertIsNotNone(result)
        self.assertEqual(result['ip'], '100.34.17.233')
        self.assertEqual(result['country'], 'NO')
        self.assertEqual(result['method'], 'GET')
        self.assertEqual(result['path'], '/news/grammy-nominations-2024')
        self.assertEqual(result['status'], '302')
        self.assertEqual(result['useragent'].startswith('Mozilla/5.0'), True)
        self.assertEqual(result['responsetime'], '269')

    def test_parse_log_line_invalid(self):
        # An invalid log line should return None
        line = 'invalid log line that does not match'
        result = parse_log_line(line)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
