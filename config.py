"""
Конфигурация для сканера портов
"""
import os
from typing import List

class Config:
    # Настройки сканирования
    DEFAULT_TIMEOUT = 1.0  # таймаут в секундах
    SCAN_DELAY = 0.1  # задержка между сканированием портов
    MAX_RETRIES = 3  # максимальное количество попыток
    
    # Порты для сканирования по умолчанию
    DEFAULT_PORTS = [
        20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139,
        143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723,
        3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000
    ]
    
    # Популярные диапазоны портов
    PORT_RANGES = {
        "well_known": list(range(1, 1025)),      # 1-1024
        "registered": list(range(1025, 49152)),  # 1025-49151
        "dynamic": list(range(49152, 65536))     # 49152-65535
    }
    
    # Настройки логирования
    LOG_FILE = "scan_log.txt"
    LOG_LEVEL = "INFO"
    
    # Настройки базы данных
    DATABASE_URL = "sqlite:///open_ports.db"
    
    # Настройки вывода
    SHOW_PROGRESS = True
    SHOW_DETAILS = True
    
    @classmethod
    def get_ports_from_range(cls, range_name: str) -> List[int]:
        """Получить список портов по названию диапазона"""
        return cls.PORT_RANGES.get(range_name, cls.DEFAULT_PORTS)
    
    @classmethod
    def get_ports_from_custom_range(cls, start: int, end: int) -> List[int]:
        """Получить список портов из пользовательского диапазона"""
        if start < 1 or end > 65535 or start > end:
            raise ValueError("Некорректный диапазон портов. Должно быть: 1 <= start <= end <= 65535")
        return list(range(start, end + 1))
    
    @classmethod
    def get_common_ports(cls) -> List[int]:
        """Получить список наиболее популярных портов"""
        return [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 5432, 8080]



