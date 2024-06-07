from sensor.exception import SensorException
from sensor.logger import logging
import os
import sys
from sensor.utils2 import dump_csv_to_mongodb
from sensor.pipeline.training_pipeline import TrainPipeline

training_pipeline = TrainPipeline()
training_pipeline.run_train_pipeline()

if __name__ == "__main__":

    file_path = "aps_failure_training_set1.csv"
    database_name = "sensor-fault"
    collection_name = "sensor"

    dump_csv_to_mongodb(file_path, database_name, collection_name)
