from sensor.exception import SensorException
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
import os
import sys
from sensor.utils2 import dump_csv_to_mongodb

training_pipeline = TrainPipeline()
training_pipeline.run_train_pipeline()
