import socket
import logging
import time
from dataclasses import dataclass
from datetime import datetime
from tqdm import tqdm


@dataclass
class PortScanner:
    host: str
    ports: list

    def __post_init__(self):
        logging.basicConfig(filename="scan_log.txt", level=logging.INFO)

    def _is_port_open(self, port: int) -> bool:
        s = socket.socket()
        s.settimeout(1)  # ставим тайм-аут в одну секунду
        # Ловим ошибки
        try:
            # Пробуем соединиться, хост и порт передаем как список
            s.connect((self.host, port))
            return True
        except socket.error:
            # тогда ничего не делаем
            return False
        finally:
            s.close()  # Закрываем соединение

    def scan_ports(self):
        print("Ожидайте, идет сканирование портов!")
        # В цикле перебираем порты из списка
        for port in tqdm(self.ports, desc="Сканирование портов"):
            print(f" Сканирую порт: {port}")
            time.sleep(0.1)
            # Создаем сокет
            if self._is_port_open(port):
                message = f"{self.host}: {port} порт активен"
                open_ports.append(port)
                print(message)
                logging.info(message)
        print("Сканирование завершено")
        return {"host": self.host,
                "open_ports": open_ports,
                "timestamp": datetime.now()
                }
