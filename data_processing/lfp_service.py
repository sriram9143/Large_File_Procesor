from data_processing.lfp_method_init_impl import LfpMethodInitImpl
from data_processing.log_utils import logger
import data_processing.config as config


class LfpService():
    step_nm = "file Load process"

    def __init__(self):
        self.Lmii = LfpMethodInitImpl()

    def run_key(self):
        logger.info("Getting Input file path and database path")
        data_file, database_file = self.Lmii.initializedirectories()

        try:
            # Initialize SQLite database connection
            conn = self.Lmii.create_connection(database_file)

            # Get data from csv.gz file
            data = self.Lmii.load_file(data_file)

            # Loading data into product table
            self.Lmii.load_table(config.FP_tableName, conn, data)

            # Creating aggregate product table.
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE IF NOT EXISTS {config.Agg_tableName} as select name, count(*) as count from "
                        f"{config.FP_tableName} group by name")

            logger.info(f"{config.Agg_tableName}  is created and loaded with aggregate data")

            self.Lmii.get_sample_of_agg_table(cur)

        except Exception as err:
            logger.error(">>>>Failed file load process %s", err)
            raise err

        finally:
            if conn:
                logger.info("SQLite {sqlite3.version} has been shutdown")
                conn.close()

        return 0
