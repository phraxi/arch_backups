import torch
import torch.nn as nn
import torch.nn.functional as f

class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.lin1 = nn.Linear(10,10)
        self.lin2 = nn.Linear(10,10)

    def forward(self, x):
        x = F.relu()
    def num_flat_features(self, x):
        pass

def main():
    net= MyNet()
    print(net)

if __name__ == "__main__":
    main()

