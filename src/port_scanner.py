import logging
import os
import socket
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

from tqdm import tqdm

from config import Config

# Добавляем родительскую директорию в путь для импорта config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@dataclass
class PortScanner:
    host: str
    ports: List[int] = None
    timeout: float = None
    scan_delay: float = None
    max_retries: int = None
    show_progress: bool = None
    show_details: bool = None

    def __post_init__(self):
        # Устанавливаем значения по умолчанию из конфигурации
        self.ports = self.ports or Config.DEFAULT_PORTS
        self.timeout = self.timeout or Config.DEFAULT_TIMEOUT
        self.scan_delay = self.scan_delay or Config.SCAN_DELAY
        self.max_retries = self.max_retries or Config.MAX_RETRIES
        self.show_progress = (
            self.show_progress
            if self.show_progress is not None
            else Config.SHOW_PROGRESS
        )
        self.show_details = (
            self.show_details if self.show_details is not None else Config.SHOW_DETAILS
        )

        # Настройка логирования
        logging.basicConfig(
            filename=Config.LOG_FILE,
            level=getattr(logging, Config.LOG_LEVEL),
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

        # Валидация входных данных
        self._validate_inputs()

    def _validate_inputs(self):
        """Валидация входных параметров"""
        if not self.host:
            raise ValueError("Хост не может быть пустым")

        if not self.ports:
            raise ValueError("Список портов не может быть пустым")

        if self.timeout <= 0:
            raise ValueError("Таймаут должен быть положительным числом")

        if self.scan_delay < 0:
            raise ValueError("Задержка сканирования не может быть отрицательной")

    def _is_port_open(self, port: int) -> bool:
        """Проверка, открыт ли порт"""
        for attempt in range(self.max_retries):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)

            try:
                s.connect((self.host, port))
                return True
            except socket.error as e:
                if attempt == self.max_retries - 1:
                    logging.debug(
                        f"Порт {port} закрыт после {self.max_retries} попыток: {e}"
                    )
                continue
            finally:
                s.close()

        return False

    def scan_ports(self) -> Dict[str, Any]:
        """Сканирование портов"""
        print(f"Начинаю сканирование {self.host}")
        print(f"Количество портов для сканирования: {len(self.ports)}")
        print(f"Таймаут: {self.timeout}с, Задержка: {self.scan_delay}с")
        print("-" * 50)
        print("💡 Нажмите Ctrl+C для прерывания сканирования")
        print("-" * 50)

        open_ports = []
        start_time = time.time()
        scanned_ports = 0

        # Создаем прогресс-бар если включен
        if self.show_progress:
            port_iterator = tqdm(self.ports, desc="Сканирование портов")
        else:
            port_iterator = self.ports

        try:
            for port in port_iterator:
                if self.show_details:
                    print(f"Сканирую порт: {port}")

                if self._is_port_open(port):
                    message = f"{self.host}: {port} порт активен"
                    open_ports.append(port)
                    print(f"✅ {message}")
                    logging.info(message)

                scanned_ports += 1

                # Задержка между сканированием
                if self.scan_delay > 0:
                    time.sleep(self.scan_delay)

        except KeyboardInterrupt:
            print("\n\n⏹️  Сканирование прервано пользователем (Ctrl+C)")
            print(f"📊 Просканировано портов: {scanned_ports}/{len(self.ports)}")
            logging.info(f"Сканирование прервано пользователем на порту {port}")

        end_time = time.time()
        scan_duration = end_time - start_time

        print("-" * 50)
        print(f"Сканирование завершено за {scan_duration:.2f} секунд")
        print(f"Просканировано портов: {scanned_ports}/{len(self.ports)}")
        print(f"Найдено открытых портов: {len(open_ports)}")

        if open_ports:
            print("Открытые порты:")
            for port in sorted(open_ports):
                print(f"  • {port}")

        return {
            "host": self.host,
            "open_ports": open_ports,
            "total_ports": len(self.ports),
            "scanned_ports": scanned_ports,
            "scan_duration": scan_duration,
            "timestamp": datetime.now(),
            "interrupted": scanned_ports < len(self.ports),
            "settings": {
                "timeout": self.timeout,
                "scan_delay": self.scan_delay,
                "max_retries": self.max_retries,
            },
        }

    def scan_common_ports(self) -> Dict[str, Any]:
        """Сканирование только популярных портов"""
        self.ports = Config.get_common_ports()
        return self.scan_ports()

    def scan_port_range(self, start: int, end: int) -> Dict[str, Any]:
        """Сканирование диапазона портов"""
        self.ports = Config.get_ports_from_custom_range(start, end)
        return self.scan_ports()

    def scan_well_known_ports(self) -> Dict[str, Any]:
        """Сканирование хорошо известных портов (1-1024)"""
        self.ports = Config.get_ports_from_range("well_known")
        return self.scan_ports()
