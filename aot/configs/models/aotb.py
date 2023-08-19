import os
from aot.configs.models.default import DefaultModelConfig

class ModelConfig(DefaultModelConfig):
    def __init__(self):
        super().__init__()
        self.MODEL_NAME = 'AOTB'

        self.MODEL_LSTT_NUM = 3
