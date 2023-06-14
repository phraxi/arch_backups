import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import openai

class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.lin1 = nn.Linear(10,10)
        self.lin2 = nn.Linear(10,10)
    def forward(self, x):
        pass
    def num_flat_features(self, x):
        pass

def main():
    net= MyNet()
    print(net)

if __name__ == "__main__":
    main()

