# PortScan
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-WIP-yellow.svg)]()

A fast, simple, multi-threaded port scanner built in Python.

---

## Features
- ✅ Multi-threaded scanning for speed.
- ✅ Custom host, port range, timeout, and thread count.
- ⏳ CLI Helper.
- ⏳ support for top common ports and service banners.
- ⏳ Low-level port scan (SYN/FIN/NULL/XMAS scans)

## Usage
```bash
git clone git@github.com:lucasdutradev/PortScan.git
cd PortScan

python3 scan.py --host 127.0.0.1 -p 1 1024
```


| Flag             | Description                        | Status        |
| ---------------- | ---------------------------------- | ------------- |
| `--host, -H`     | Target host (hostname or IP)       | ✅ Working     |
| `--timeout, -T`  | Timeout per request                | ✅ Working     |
| `--threads, -TH` | Number of threads to use           | ✅ Working     |
| `--ports, -p`    | Port range, e.g. `-p 1 200`        | ✅ Working     |
| `--top-ports`    | Scan top N most common ports       | ⏳ In progress |
| `--verbose`      | Show port banner (HTTP, SSH, etc.) | ⏳ In progress |

# Disclaimer

This project is for educational purposes only.
Do not scan hosts you don’t own or have permission to test.