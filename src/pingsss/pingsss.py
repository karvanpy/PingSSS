import subprocess
import ipaddress
import argparse
import concurrent.futures
import json
import os
import logging
from colorama import init, Fore

# Initialize colorama
init()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PingSSS:
    def __init__(self, ip_range, show='all', output=None):
        self.ip_range = ip_range
        self.show = show
        self.output = output
        self.results = {}

    def ping_host(self, host):
        """
        Ping a host and return True if it's reachable, False otherwise.
        """
        try:
            subprocess.check_output(['ping', '-c', '1', str(host)])
            return host, True
        except subprocess.CalledProcessError:
            return host, False

    def parse_ip_range(self):
        """
        Parse an IP range (e.g., 192.168.100.1-20) and return a list of IP addresses.
        """
        try:
            start_ip, end_ip = self.ip_range.split('-')
            start_ip = ipaddress.ip_address(start_ip)
            end_ip = ipaddress.ip_address(start_ip.packed[:3] + bytes([int(end_ip)]))

            return [ipaddress.ip_address(start_ip.packed[:3] + bytes([i])) for i in range(int(start_ip.packed[3]), int(end_ip.packed[3]) + 1)]
        except ValueError as e:
            logging.error(f"Invalid IP range: {e}")
            return []

    def run(self):
        hosts = self.parse_ip_range()

        while not hosts:
            self.ip_range = input("Enter IP range: ")
            hosts = self.parse_ip_range()

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.ping_host, host): host for host in hosts}
            for future in concurrent.futures.as_completed(futures):
                host = futures[future]
                try:
                    host, reachable = future.result()
                    self.results[str(host)] = reachable
                    if self.show == 'all' or (self.show == 'alive' and reachable) or (self.show == 'dead' and not reachable):
                        logging.info(f"{Fore.GREEN if reachable else Fore.RED}Host {host} {'alive' if reachable else 'dead'}{Fore.RESET}")
                except Exception as e:
                    logging.error(f"Error pinging host {host}: {e}")

        if self.output == 'json':
            self.save_results_to_json()

        self.print_summary()

    def save_results_to_json(self):
        filename = 'output.json'
        i = 1
        while os.path.exists(filename):
            filename = f'output{i}.json'
            i += 1
        with open(filename, 'w') as f:
            json.dump(self.results, f)

    def print_summary(self):
        alive_count = sum(1 for result in self.results.values() if result)
        dead_count = len(self.results) - alive_count
        logging.info(f"Finished: alive [{alive_count}] | dead [{dead_count}]")

def main():
    parser = argparse.ArgumentParser(description='Ping multiple hosts concurrently.')
    parser.add_argument('ip_range', help='IP range to ping (e.g., 192.168.100.1-20)')
    parser.add_argument('--output', choices=['json'], help='Save output to file in JSON format')
    parser.add_argument('--show', choices=['all', 'alive', 'dead'], default='all', help='Show only alive or dead hosts')
    args = parser.parse_args()

    ping_tool = PingSSS(args.ip_range, args.show, args.output)
    ping_tool.run()

if __name__ == "__main__":
    main()
