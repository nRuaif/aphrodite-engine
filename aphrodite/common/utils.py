"""Utils."""
import enum
from platform import uname
import uuid

import psutil
import torch

class Device(enum.Enum):
    GPU = enum.auto()
    CPU = enum.auto()

class Counter:
    '''A basic counter.'''
    def __init__(self, start: int = 0) -> None:
        self.counter = start

    def __next__(self) -> int:
        id = self.counter
        self.counter += 1
        return id

    def reset(self) -> None:
        self.counter = 0


def get_gpu_memory(gpu: int = 0) -> int:
    """Returns the total memory of the GPU in bytes."""
    return torch.cuda.get_device_properties(gpu).total_memory

def get_cpu_memory() -> int:
    """Returns the total CPU memory of the node in bytes."""
    return psutil.virtual_memory().total

def random_uuid() -> str:
    return str(uuid.uuid4().hex)

def in_wsl() -> bool:
    return "microsoft" in " ".join(uname()).lower()