# coding: utf-8

import torch

torch.save({"user": [1, 2, 3]}, "test.pt")
print(torch.load("test.pt"))
