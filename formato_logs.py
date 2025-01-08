import logging

#damos formatos al logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

nombre = "Choni"
logging.error(f"{nombre} creó el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")

try:
    division = 2 / 0
except:
    #mostrar solo el msj
    logging.error("Division por cero")
    #mostrar con mas profundidad el error
    logging.exception("División por cero")
