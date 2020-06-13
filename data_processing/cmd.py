import sys
import time
import memory_profiler as mem_profile
from data_processing.log_utils import logger
from data_processing.lfp_service import LfpService


def main():
    main_rc = -1
    content = list()
    subject = "Performance check:"

    try:
        content.append('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB')
        t1 = time.process_time()

        srvc = LfpService()
        logger.info("Starting : %s", srvc.step_nm)

        main_rc = srvc.run_key()


        t2 = time.process_time()
        content.append('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')
        content.append('Took ' + str(t2 - t1) + ' Seconds')
        logger.info(subject)
        total = f'{content[0]}\t{content[1]}\t{content[2]}'
        logger.info(total)
        logger.info("Large_file_process is completed")
        print("\n"+'Took ' + str(t2 - t1) + ' Seconds to complete')

    except Exception as err:
        logger.error(">>>The program failed with the following error %s", err)
        raise Exception

    return main_rc


if __name__ == '__main__':
    sys.exit(main())
