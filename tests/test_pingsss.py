import unittest
from src.pingsss.pingsss import PingSSS


class TestPingTool(unittest.TestCase):
    def test_parse_ip_range(self):
        pingsss = PingSSS('192.168.100.1-20')
        ip_list = pingsss.parse_ip_range()
        self.assertEqual(len(ip_list), 20)
        self.assertEqual(str(ip_list[0]), '192.168.100.1')
        self.assertEqual(str(ip_list[-1]), '192.168.100.20')

    def test_invalid_ip_range(self):
        pingsss = PingSSS('invalid-ip-range')
        ip_list = pingsss.parse_ip_range()
        self.assertEqual(len(ip_list), 0)

if __name__ == '__main__':
    unittest.main()
