import platform
import sys

from config import settings


def create_allure_environment_file():
    environment_data = {
        "os_info": f"{platform.system()}, {platform.release()}",
        "python_version": sys.version,
    }
    environment_data.update(settings.model_dump())
    items = [f"{key}={value}" for key, value in environment_data.items()]
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
