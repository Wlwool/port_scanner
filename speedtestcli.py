import subprocess
import os
import datetime
import json

filename = "speedtest_results.txt"

# Проверяем, существует ли файл с указанным именем, если нет, создаем пустой файл
if not os.path.exists(filename):
    open(filename, "w").close()

# Запуск Speedtest CLI и получение результатов
result = subprocess.run(["speedtest", "--json"], capture_output=True, text=True)
# print(f"Получен результат: {result}")

# Проверка на ошибки при выполнении speedtest
if result.returncode != 0:
    print(f"Ошибка запуска SpeedTest: {result.stderr.strip()}")
else:
    # data = json.loads(result.stdout.strip())  # Преобразование JSON-строки в объект Python
    data = result.stdout.strip()        # Получение данных о скорости и времени тестирования
    # ping = data["ping"]["value"]
    # download_speed = data["download"]["bandwidth"]
    # upload_speed = data["upload"]["bandwidth"]
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:      # Добавление результатов в файл
        f.write(f"{timestamp} {data}\n")

    # print(f"Пинг: {ping} ms")
    # print(f"Скорость загрузки: {download_speed / 1_000_000:.2f} Mbps")
    # print(f"Скорость отдачи: {upload_speed / 1_000_000:.2f} Mbps")
