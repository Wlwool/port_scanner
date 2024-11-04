from src.port_scanner import PortScanner
from database.database import create_database, save_report


if __name__ == '__main__':
    host = input('Введи имя сайта без http/https или IP-адрес: ')
    # Список портов для сканирования
    ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139,
             143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723,
             3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000
             ]
    create_database()
    scanner = PortScanner(host, ports)
    report = scanner.scan_ports()

    save_report(report)
