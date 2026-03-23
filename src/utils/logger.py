import logging
import sys


def setup_logging(level="INFO"):
    """Настройка логирования для всего проекта."""
    log_format = "%(asctime)s [%(levelname)-8s] %(name)-20s: %(message)s"

    root = logging.getLogger()
    root.setLevel(getattr(logging, level))

     # Консоль
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(logging.Formatter(log_format, datefmt="%H:%M:%S"))
    root.addHandler(console)

    # Приглушаем шумные библиотеки
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    return root
