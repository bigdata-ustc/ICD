# coding: utf-8

import torch

print(torch.min(torch.tensor([1, 2, 3]) * (1 - torch.tensor([2, 1, -1]))))
