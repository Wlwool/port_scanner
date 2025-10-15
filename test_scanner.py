#!/usr/bin/env python3
"""
Тестовый скрипт для демонстрации возможностей сканера портов
"""
from database.db import create_database, save_report
from src.port_scanner import PortScanner


def test_different_modes():
    """Тестирование различных режимов сканирования"""
    host = "google.com"

    print("🧪 Тестирование различных режимов сканирования")
    print("=" * 60)
    print("💡 Нажмите Ctrl+C в любой момент для прерывания")
    print("=" * 60)

    try:
        # БД
        create_database()

        # Тест 1: Быстрое сканирование популярных портов
        print("\n🔍 Тест 1: Быстрое сканирование популярных портов")
        scanner1 = PortScanner(
            host=host, timeout=0.5, scan_delay=0.05, show_details=False
        )
        report1 = scanner1.scan_common_ports()
        if not report1.get("interrupted", False):
            save_report(report1)

        # Тест 2: Сканирование диапазона 80-443
        print("\n🔍 Тест 2: Сканирование диапазона 80-443")
        scanner2 = PortScanner(
            host=host, timeout=1.0, scan_delay=0.1, show_details=True
        )
        report2 = scanner2.scan_port_range(80, 443)
        if not report2.get("interrupted", False):
            save_report(report2)

        # Тест 3: Сканирование с настройками по умолчанию
        print("\n🔍 Тест 3: Сканирование с настройками по умолчанию")
        scanner3 = PortScanner(host=host)
        report3 = scanner3.scan_ports()
        if not report3.get("interrupted", False):
            save_report(report3)

        print("\n✅ Все тесты завершены!")

    except KeyboardInterrupt:
        print("\n\n⏹️  Тестирование прервано пользователем")
        print("👋 До свидания!")
        exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка во время тестирования: {e}")
        exit(1)


if __name__ == "__main__":
    test_different_modes()
