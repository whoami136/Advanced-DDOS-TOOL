![Uploading Screenshot_2026-06-25_16_12_09.png…]()

# Advanced-DDOS-TOOL
This Tool Is for Educational purposes So Dont missuse it
 Sentry-Loris Far better than slowloris more faster more stable works with proxychains after -10k connection it will crash server
Sentry-Loris is an asynchronous Python-based security tool designed to test the resilience of web servers against Slow HTTP DoS attacks. It specifically implements the "Slowloris" methodology, which operates at the Application Layer (Layer 7) by exhausting a server’s concurrent connection pool.

Key Features:
Asynchronous Architecture: Built using asyncio to manage a large number of concurrent connections with minimal system resource consumption.

Protocol Testing: Targets HTTP service availability by maintaining incomplete request headers and periodic "keep-alive" data.

Customizable Parameters: Allows for manual configuration of target hosts, specific ports, socket concurrency levels, and header sleep intervals.

User-Agent Randomization: Cycles through various browser signatures to simulate diverse traffic patterns.

Disclaimer
This tool is intended strictly for authorized security auditing and educational purposes only. Unauthorized use of this tool against targets without explicit permission is illegal and unethical. The developer assumes no responsibility for any misuse or damage caused by this program.
### Getting Started

After cloning the repository, navigate into the directory and verify the contents:

```bash
cd Advanced-DDOS-TOOL
ls
python3  ddos.py -p Port -s socket/packets IP
Example : python3  ddos.py -p 80 -s 150 102.0.0.1 
