import logging
import logging.config

logging.config.fileConfig('logging.conf')
#使用字典就能从任意格式文件进行配置，字典是一种接口格式
# logging.config.dictConfig({"loggers":"root,applog"})

rootLogger = logging.getLogger()
rootLogger.debug("This is root Logger, debug")

logger = logging.getLogger('applog')
logger.debug("This is applog, debug")

try:
    int(a)
except Exception as e:
    logger.exception(e)