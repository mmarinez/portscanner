import socket
import argparse

# Initial socket connection through IPv4 and TCP
def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        sock.close()

        return result == 0
    except Exception as e:
        print(e)
        return False


# Argument Parser
def parse_and_parser_builder():
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("target", help="Target IP or hostname to scan")
    parser.add_argument("-port", "--ports", 
                        help="Ports to scan. Single(80), comma list (22,80,443), or range (1-1024). Default: 1-1024",
                        default="1-1024")
    parser.add_argument("-t", "--timeout",
                        help="Socket timeout in seconds (default: 1)",
                        type=float, default=1.0)
    return parser.parse_args()


# Port argument parser
def parse_ports(ports_arg: str) -> list[int]:
    """
        Accepts: 
            "80" -> [80]
            "22,80,443" -> [22,80,443]
            "1-1024" -> list(range(1,1025))
    """ 
         
    parts = [p.strip() for p in ports_arg.split(",") if p.strip()]
    ports = set()
    for part in parts:
        if "-" in part:
            start_str, end_str = part.split("-", 1)
            start = int(start_str)
            end = int(end_str)
            for p in range(start, end + 1):
                if 1 <= p <= 65535:
                    ports.add(p)
        else:
            p = int(part)
            if 1 <= p <= 65535:
                ports.add(p)
    return sorted(ports)


def main():
    args = parse_and_parser_builder()
    target = args.target
    port_list = parse_ports(args.ports)

    print(f"Scanning {target} with timeout=1 on {len(port_list)} ports...")
    for port in port_list:
        is_open = scan_port(target, port)
        if is_open:
            print(f"[+] Port {port} OPEN")
        else:
            print(f"[-] Port {port} closed")


if __name__ == "__main__":
    main()