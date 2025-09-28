import socket
import argparse

class portscanner:

    # Initial socket connection through IPv4 and TCP
    def scan_port(host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connectex((host, port))
            sock.close()

            return result
        except Exception as e:
            print(e)
            return False

    # Argument Parser
    def parse_and_parser_builder():
        parser = argparse.ArgumentParser(description="Simple TCP port scanner")
        parser.add_argument("target", help="Target IP or hostname to scan")
        parser.add_argument("port", "--ports", 
                            help="Ports to scan. Single(80), comma list (22,80,443), or range (1-1024). Default: 1-1024",
                            default="1-1024")
        parser.add_argument("-t", "--timeout",
                            help="Socket timeout in seconds (default: 1)",
                            type=float, default=1.0)
        return parser.parse_args()

    # Port argument parser
    def parse_ports():
        """
        Accepts: 
            "80" -> [80]
            "22,80,443" -> [22,80,443]
            "1-1024" -> list(range(1,1025))
        """
        pass
        