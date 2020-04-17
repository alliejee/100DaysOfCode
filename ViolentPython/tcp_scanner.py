import argparse
import nmap
from socket import *
from threading import *


screenLock = Semaphore(value=1)
# connects to host and port that's passed in    
def connectScan(target_host, target_port):
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect((target_host, target_port))
        s.send('ViolentPython\r\n')
        results = s.recv(100)
        screenLock.acquire()
        print(f"[+]{target_port}/tcp open")
        print(f"[+] {str(results)}")
        
    except:
        screenLock.acquire()
        print(f"[-]{target_port}/tcp closed")
        
    finally:
        screenLock.release()
        s.close()
        
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
        # tell thread to run connectScan method and feed it the target host and current target port
        t = Thread(target=connectScan, args=(target_host, int(target_port)))
        t.start()
        print(f"Scanning port {target_port}")
        connectScan(target_host, target_port)

def nmapScan(target_host, target_port):
    nmScan = nmap.PortScanner()
    nmScan.scan(target_host, target_port)
    state=nmScan[target_host]['tcp'][int(target_port)]['state']
    print(f" [*] {target_host} tcp/{target_port} {state}")

def main():
    parser = argparse.ArgumentParser(description="TCP Port Scanner")

    # add the host and port arguments
    parser.add_argument("-H", "--host", dest="target_host", help="host to be scanned")
    parser.add_argument("-p", "--port", dest="target_port", type=int, help="specify port[s] separate by comma")

    # store the arguments in args
    args = parser.parse_args()

    # assign the incoming parameters to variables
    target_host = args.target_host
    target_ports = str(args.target_port).split(', ')

    # check to make sure that host and port values have been supplied
    if target_host is None or target_ports is None:
        parser.print_usage()
        exit(0)

    #initiating port scan if target host and port(s) are present
    portScan(target_host, target_ports)
        
if __name__ == '__main__':
    main()
        