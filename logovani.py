import logging


logger = logging.getLogger(__name__)
#logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logger.debug("jen ladici hlaska")
logger.info("ahoj, to je informace")
logger.warning("pozor, tady je varovani")
logger.error("zasadni chyba, koncim")
logger.fatal("tak tohle je fatalni")

print("konec logovani")
