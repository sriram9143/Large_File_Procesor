import os
import pandas as pd
import data_processing.config as dirr
import sqlite3

from sqlite3 import Error
from data_processing.log_utils import logger
from data_processing.lfp_method_init import LfpMethodInit as lmi


class LfpMethodInitImpl(lmi):

    def initializedirectories(self):
        try:
            os.makedirs(dirr.database_dir, exist_ok=True)
        except Exception as err:
            raise Exception("failed to initialize data directory %s", err)
            logger.error("failed to initialize data directory %s", err)

        data_f = "products.csv.gz"
        database_nm = "test.db"
        dataFile = os.path.join(dirr.data_dir, data_f)
        databaseFile = os.path.join(dirr.database_dir, database_nm)

        logger.info(f"data file path : {dataFile}")
        logger.info(f"database path: {databaseFile}")

        return dataFile, databaseFile

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            logger.info(f"SQLite {sqlite3.version} has been initialized")
        except Error as e:
            logger.error(">>>>Failed to create connection %s", e)
            raise e
        return conn

    def load_file(self, datafile):
        """ get csv.gz file content into data variable"""
        try:
            data = pd.read_csv(datafile, compression='gzip', error_bad_lines=False)
            logger.info("data load from csv.gz is done")
        except Exception as err:
            logger.error(">>>> failed to get data with error %s",err)
            raise err

        return data

    def load_table(self, tablename, conn, data):
        """load data into table"""
        try:
            data.to_sql(tablename, conn, if_exists='append', index=False)
            logger.info(f"{tablename} table is  Successfully loaded with data")
        except Exception as err:
            logger.error(f">>>>>>failed to load data into table : {tablename}")
            raise err

    def get_sample_of_agg_table(self, cur):
        """printout sample aggregate data"""
        try:
            cur.execute("select * from product_agg limit 10")
            row = cur.fetchall()
            print("Sample Aggreagate data: ")
            for val in row:
                print(val)
            logger.info(f"sample aggregate data :{row}")
        except Exception as err:
            raise err

