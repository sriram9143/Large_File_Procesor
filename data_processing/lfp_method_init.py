from abc import ABC, abstractmethod


class LfpMethodInit(ABC):

    @abstractmethod
    def initializedirectories(self):
        pass

    @abstractmethod
    def create_connection(self, db_file):
        pass

    @abstractmethod
    def load_file(self, datafile):
        pass

    @abstractmethod
    def load_table(self, tablename, conn, data):
        pass

    @abstractmethod
    def get_sample_of_agg_table(self, cur):
        pass

