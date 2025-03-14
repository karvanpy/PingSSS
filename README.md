# PingSSS - A tool to ping multiple hosts concurrently

PingSSS is a powerful command-line tool designed to ping multiple hosts concurrently. It's perfect for network diagnostics and testing, allowing you to efficiently monitor the status of numerous devices simultaneously.

[![PyPI - Version](https://img.shields.io/pypi/v/pingsss)](https://pypi.org/project/pingsss/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/pingsss)](https://pypi.org/project/pingsss/)

[![asciicast](https://asciinema.org/a/708104.svg)](https://asciinema.org/a/708104)

## Features
* Concurrent Pinging: Ping multiple hosts at the same time to save time and effort.
* IP Range Parsing: Easily parse and ping a range of IP addresses with a simple command.
* Filter Results: Display only alive or dead hosts based on your preference.
* JSON Output: Save the results in JSON format for further analysis.

## Installation

To install PingSSS, use pip:
```
pip install pingsss
```

Alternatively, you can run PingSSS without installation using uvx:
```
uvx pingsss
```

## Usage

PingSSS is easy to use with straightforward commands. Here's a basic example:
```
pingsss 192.168.100.1-20 --output json --show alive
```

This command will ping the IP range 192.168.100.1 to 192.168.100.20, output the results in JSON format, and display only the alive hosts.

## Links

* PyPI: pypi.org/project/pingsss
* GitHub: github.com/karvanpy/pingsss

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or want to contribute code, please open an issue or submit a pull request.

## License

PingSSS is licensed under the MIT License. See the LICENSE file for more details.