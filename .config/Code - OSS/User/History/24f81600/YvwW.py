import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
import openai

def main():
    net= MyNet()
    print(net)

if __name__ == "__main__":
    main()

class MyNet(nn.Module):
    def __init(self):
        pass
    def forward(self, X):
        pass
    def num_flat_features(self, x):
        pass