import torch

from lib.networks import make_network
from lib.config.config import cfg


model = torch.load('249.pth')
print(model)
