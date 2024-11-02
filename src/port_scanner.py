import socket
from dataclasses import dataclass


@dataclass
class PortScanner:
    host: str
    ports: list

    def _is_port_open(self, port: int) -> bool:
        s = socket.socket()
        s.settimeout(1)  # ставим тайм-аут в одну секунду
        # Ловим ошибки
        try:
            # Пробуем соединиться, хост и порт передаем как список
            s.connect((self.host, port))
            # Если соединение вызвало ошибку
        except socket.error:
            # тогда ничего не делаем
            pass
        else:
            # print(f"{host}: {port} порт активен")
            # Закрываем соединение
            s.close()
            return True

    def scan_ports(self):
        print("Ожидайте, идет сканирование портов!")
        # В цикле перебираем порты из списка
        for port in self.ports:
            # Создаем сокет
            if self._is_port_open(port):
                print(f"{self.host}: {port} порт активен")
        print("Сканирование завершено")
