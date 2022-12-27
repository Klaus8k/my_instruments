import logging

logger = logging.getLogger('csv_reader')
cons_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f'csv_reader-log.txt', mode='w')
cons_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)
cons_format = logging.Formatter(
    '%(process)d: %(relativeCreated)d ms ---> %(message)s')
file_format = logging.Formatter(
    '%(asctime)s PID - %(process)d. %(relativeCreated)d ms ---> [[%(message)s]]', datefmt='%Y-%m-%d %H:%M:%S')
cons_handler.setFormatter(cons_format)
file_handler.setFormatter(file_format)

logger.addHandler(cons_handler)
logger.addHandler(file_handler)


# Логгер измеряющий время в консоль/
logger_timer = logging.getLogger('timer')
exit_handler = logging.StreamHandler()
format_formatter = logging.Formatter('%(asctime)s --- %(message)s')
exit_handler.setFormatter(format_formatter)
logger_timer.addHandler(exit_handler)