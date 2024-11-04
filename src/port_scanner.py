import socket
import logging
from dataclasses import dataclass
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
            # Создаем сокет
            if self._is_port_open(port):
                message = f"{self.host}: {port} порт активен"
                print(message)
                logging.info(message)
        print("Сканирование завершено")
