# coding: utf-8


from torch import nn


class SM1(nn.Module):
    def __init__(self):
        super(SM1, self).__init__()
        self.embedding = nn.Embedding(10, 5)
        self.fc = nn.Linear(5, 3)
        self.act = nn.Sigmoid()


class SM2(nn.Module):
    def __init__(self):
        super(SM2, self).__init__()
        self.fea = nn.Sequential(
            nn.Embedding(10, 5),
            nn.Dropout(0.2),
            nn.ReLU(),
        )


class M1(nn.Module):
    def __init__(self):
        super(M1, self).__init__()
        self.net1 = SM1()
        self.net2 = SM2()


m = M1()
for name, parameter in m.named_parameters():
    print(name)
