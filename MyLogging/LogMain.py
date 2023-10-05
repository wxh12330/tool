import logging
import logging.config

def get_log() -> logging:
	"""
		本地记录日志
	"""
	log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'LogConfig/loggingcnf.conf')
	if not os.path.isdir("/home/test/my_python/logs/"):
		os.makedirs("/home/test/my_python/logs/")
	logging.config.fileConfig(log_file_path)
	logger = logging.getLogger('policymanager')
	return logger.debug

	
if __name__ == '__main__':
	my_log = get_log()
	my_log("my logging test !!!!")