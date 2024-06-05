from sensor.exception import SensorException
from sensor.logger import logging
import os
import sys
from sensor.utils import dump_csv_to_mongodb

# def test_exception():
#     try:
#         logging.info("hello")
#
#     except Exception as e:
#         raise SensorException(e,sys)


if __name__ == "__main__":

    file_path = "aps_failure_training_set1.csv"
    database_name = "sensor-fault"
    collection_name = "sensor"

    dump_csv_to_mongodb(file_path, database_name, collection_name)

    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)