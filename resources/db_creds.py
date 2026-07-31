import os
from dotenv import load_dotenv
from pathlib import Path

# Получаем корневую директорию проекта
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

# Загружаем .env файл
load_dotenv(env_path)

# Для отладки
print(f"Ищем .env в: {env_path}")
print(f"Файл существует: {env_path.exists()}")
print(f"DB_PORT из .env: {os.getenv('DB_PORT')}")


class DBCreds:
    HOST = os.getenv('DB_HOST', 'localhost')
    USER = os.getenv('DB_USER', 'postgres')
    PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    NAME = os.getenv('DB_NAME', 'postgres')

    @staticmethod
    def get_port():
        port = os.getenv('DB_PORT', '5432')
        if port is None or str(port).lower() == 'none' or str(port).strip() == '':
            print(f"Порт '{port}' некорректен, используем 5432")
            return 5432
        try:
            return int(port)
        except (ValueError, TypeError):
            print(f"Не удалось преобразовать порт '{port}', используем 5432")
            return 5432

    PORT = get_port()