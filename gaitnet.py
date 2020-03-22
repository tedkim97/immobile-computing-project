import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import sampler

class gaitAccelNet(nn.Module):
    """
    Our torch model that represents our gait classifier
    Simple classifier consistenting of 2 convolutional layers 
                                        1 maxpool layer and 
                                        2 fully connected layers 
    """
    def __init__(self, n_people=3):
        super(gaitAccelNet, self).__init__()
        self.conv1 = nn.Conv2d(13, 52, 1)
        self.conv2 = nn.Conv2d(52, 104, (1,3))
        self.pool = nn.MaxPool2d(1,1)    
        self.fc1 = nn.Linear(104, 10)
        self.fc2 = nn.Linear(10, n_people) 
        #last layer should be the number of potential outputs we have
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.pool(x).squeeze()
#         print('maxpool after shape =', x.shape)
        x = self.fc1(x)
        x = self.fc2(x)
        return x
