from datetime import datetime
import os
import sys
from sensor.exception import SensorException
from sensor.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self, timestamp:datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%S")

        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp = timestamp

class DataIngestionConfig:
    try:
        pass
    except Exception as e:
        raise SensorException(e, sys)