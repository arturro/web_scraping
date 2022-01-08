from os import path
import logging.config

file_path = path.join(path.dirname(path.abspath('04_file.conf')), '04_file.conf')
logging.config.fileConfig(file_path)

logger = logging.getLogger(__name__)

logger.debug('gdzie trafi debug')
logger.info('gdzie info?')
