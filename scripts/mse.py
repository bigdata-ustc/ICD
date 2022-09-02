# coding: utf-8
# 2022/2/3 @ tongshiwei

import torch
from torch import nn

mse_loss = nn.MSELoss()

print(mse_loss(
    torch.tensor([[1., 2], [3, 4]]),
    torch.tensor([[1., 3], [4, 4]])
))

print(mse_loss(
    torch.tensor([[2.], [3]]),
    torch.tensor([[3.], [4]])
))
