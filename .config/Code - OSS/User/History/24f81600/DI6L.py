import torch
from torch.nn import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import openai

class MyNet(nn.Module):
    def __init__(self):
        pass
    def forward(self, x):
        pass
    def num_flat_features(self, x):
        pass

def main():
    net= MyNet()
    print(net)

if __name__ == "__main__":
    main()

