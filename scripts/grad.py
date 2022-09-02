# coding: utf-8

import torch
from torch import nn


class A(nn.Module):
    def __init__(self):
        super(A, self).__init__()
        self.emb = nn.Embedding(4, 4)

    def forward(self, x: torch.Tensor):
        y = self.emb(x)
        return y


class B(nn.Module):
    def __init__(self):
        super(B, self).__init__()

    def forward(self, y: torch.Tensor):
        return (2 * y).sum()


a = A()
b = B()
a.eval()
x = torch.tensor([1, 2, 3])
y: torch.Tensor = a(x).detach()
y.requires_grad_(True)
b(y).backward()
print(y.grad)
