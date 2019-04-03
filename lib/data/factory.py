import torch
from lib.config.paths import PATHS
# from .datasets.df import OpenWorldNoDef

from .datasets.coco import COCO


class DatasetFactory:
    
    def __init__(self, cfg):
        self.cfg = cfg
        
    def get(self, name: str):
        """
        """
        factory = None
        args = {}
        if 'COCO' in name:
            # COCO.train, COCO.val
            # name: COCO, mode: 'train', 'val'
            name, _, mode = name.partition('.')
            factory = COCO
            args = {
                'root': PATHS[name]['root'],
                'mode': mode,
                'num_kps': self.cfg.DATASET.COCO.KPS,
                'size': (self.cfg.DATASET.COCO.HEIGHT, self.cfg.DATASET.COCO.WIDTH)
            }

        return factory, args
    