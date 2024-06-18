from sensor.exception import SensorException
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
import os
import sys
from sensor.utils2 import dump_csv_to_mongodb

# set_env_variable(env_file_path)

training_pipeline = TrainPipeline()
training_pipeline.run_pipeline()
