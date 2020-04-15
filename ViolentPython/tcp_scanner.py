import argparse

from socket import *

parser = argparse.ArgumentParser(description="TCP Port Scanner")

parser.add_argument("-H", "--host", dest="target_host", help="host to be scanned")
parser.add_argument("-p", "--port", dest="target_port", type=int, help="port to be scanned")

args = parser.parse_args()
target_host = args.target_host
target_port = args.target_port

if target_host is None or target_port is None:
    parser.print_usage()
    exit(0)
    
def connectScan(target_host, target_port):
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect((target_host, target_port))
        print(f"[+]{target_port}/tcp open")
        s.close()
        
    except:
        print(f"[-]{target_port}/tcp closed")
        
def portScan(target_host, target_ports):
    try:
        target_IP = gethostbyname(target_host)
    except:
        print(f"[-] Cannot resolve {target_host}: Unkown host")
        return
    try:
        target_name = gethostbyaddr(target_IP)
        print(f"\n[+] Scan Results for: {target_name[0]}")
    except:
        print(f"\n[+] Scan Results for: {target_IP}")
    setdefaulttimeout(1)
    for target_port in target_ports:
        print(f"Scanning port {target_port}")
        connectScan(target_host, target_port)