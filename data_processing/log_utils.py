import logging
import os

import data_processing.config as dirr

try:
    os.makedirs(dirr.log_dir, exist_ok=True)
    log_f = 'lfp.log'
    file_name = os.path.join(dirr.log_dir, log_f)
    logger = logging
    log_format = f'%(asctime)-2s - %(name)-2s - %(levelname)-3s: %(message)s'
    logger.basicConfig(filename=file_name, format=log_format, level=logging.INFO)

except Exception as e:
            raise e
