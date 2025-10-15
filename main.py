from config import Config
from database.db import create_database, save_report
from src.port_scanner import PortScanner


def get_scan_mode():
    """Выбор режима сканирования"""
    print("\n🎯 Выберите режим сканирования:")
    print("1. Стандартное сканирование (все порты)")
    print("2. Сканирование популярных портов")
    print("3. Сканирование диапазона портов")
    print("4. Сканирование хорошо известных портов (1-1024)")

    while True:
        try:
            choice = input("Введите номер (1-4): ").strip()
            if choice in ["1", "2", "3", "4"]:
                return choice
            print("❌ Пожалуйста, введите число от 1 до 4")
        except KeyboardInterrupt:
            print("\n\n👋 До свидания!")
            exit(0)


def get_custom_range():
    """Получение пользовательского диапазона портов"""
    while True:
        try:
            start = int(input("Введите начальный порт (1-65535): "))
            end = int(input("Введите конечный порт (1-65535): "))

            if 1 <= start <= 65535 and 1 <= end <= 65535 and start <= end:
                return start, end
            else:
                print("❌ Некорректный диапазон портов")
        except ValueError:
            print("❌ Пожалуйста, введите корректные числа")
        except KeyboardInterrupt:
            print("\n\n👋 До свидания!")
            exit(0)


def get_scan_settings():
    """Получение пользовательских настроек сканирования"""
    print("\n⚙️  Настройки сканирования:")

    # Таймаут
    try:
        timeout_input = input(
            f"Таймаут в секундах (по умолчанию {Config.DEFAULT_TIMEOUT}): "
        ).strip()
        timeout = float(timeout_input) if timeout_input else Config.DEFAULT_TIMEOUT
    except ValueError:
        print(f"❌ Некорректный таймаут, используем {Config.DEFAULT_TIMEOUT}")
        timeout = Config.DEFAULT_TIMEOUT
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        exit(0)

    # Задержка
    try:
        delay_input = input(
            f"Задержка между сканированием в секундах (по умолчанию {Config.SCAN_DELAY}): "
        ).strip()
        scan_delay = float(delay_input) if delay_input else Config.SCAN_DELAY
    except ValueError:
        print(f"❌ Некорректная задержка, используем {Config.SCAN_DELAY}")
        scan_delay = Config.SCAN_DELAY
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        exit(0)

    # Детали
    try:
        details_input = (
            input("Показывать детали сканирования? (y/n, по умолчанию y): ")
            .strip()
            .lower()
        )
        show_details = details_input != "n" if details_input else True
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        exit(0)

    return timeout, scan_delay, show_details


def get_host_input():
    """Получение хоста от пользователя"""
    try:
        host = input("Введите имя сайта без http/https или IP-адрес: ").strip()
        if not host:
            print("❌ Хост не может быть пустым")
            exit(1)
        return host
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        exit(0)


def perform_scan(scanner, mode):
    """Выполнение сканирования в зависимости от выбранного режима"""
    if mode == "1":
        print(
            f"\n🔍 Стандартное сканирование " f"{len(Config.DEFAULT_PORTS)} портов..."
        )
        return scanner.scan_ports()
    elif mode == "2":
        print(
            f"\n🔍 Сканирование "
            f"{len(Config.get_common_ports())} популярных портов..."
        )
        return scanner.scan_common_ports()
    elif mode == "3":
        start, end = get_custom_range()
        print(
            f"\n🔍 Сканирование диапазона {start}-{end} ({end - start + 1} портов)..."
        )
        return scanner.scan_port_range(start, end)
    else:  # mode == "4"
        print("\n🔍 Сканирование хорошо известных портов (1-1024)...")
        return scanner.scan_well_known_ports()


def save_scan_results(report):
    """Сохранение результатов сканирования"""
    if not report.get("interrupted", False):
        save_report(report)
        print(f"\n💾 Результат сохранен в базу данных {Config.DATABASE_URL}")
    else:
        print(
            f"\n⚠️  Сканирование было прервано, результат не сохранен "
            f"{Config.DATABASE_URL}"
        )


def main():
    """Главная функция программы"""
    print("🚀 Сканер портов v2.0")
    print("=" * 50)

    # Получаем входные данные
    host = get_host_input()
    mode = get_scan_mode()
    timeout, scan_delay, show_details = get_scan_settings()

    # База данных
    create_database()

    # Сканер с настройками
    scanner = PortScanner(
        host=host, timeout=timeout, scan_delay=scan_delay, show_details=show_details
    )

    # Сканирование
    try:
        report = perform_scan(scanner, mode)
        save_scan_results(report)
    except KeyboardInterrupt:
        print("\n\n⏹️  Сканирование прервано пользователем")
        exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 До свидания!")
        exit(0)
