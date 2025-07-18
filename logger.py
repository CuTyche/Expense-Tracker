import logging
#Basic Configuration of the logger
logging.basicConfig(
  filename='tracker.log',
  filemode='w',
  level=logging.DEBUG,

  format ='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
  datefmt='%Y-%M-%d %H:%M:%S'
)

def get_logger():
  return logging.getLogger()