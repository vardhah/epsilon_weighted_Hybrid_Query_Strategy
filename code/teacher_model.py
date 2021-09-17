import torch.nn as nn
import torch.nn.functional as F

HIDDEN1_UNITS = 256
HIDDEN2_UNITS = 128
HIDDEN3_UNITS = 64
HIDDEN4_UNITS = 32
HIDDEN5_UNITS = 16

class TNet(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, HIDDEN1_UNITS)
        self.fc2 = nn.Linear(HIDDEN1_UNITS, HIDDEN2_UNITS)
        self.fc3 = nn.Linear(HIDDEN2_UNITS, HIDDEN3_UNITS)
        self.fc4 = nn.Linear(HIDDEN3_UNITS, HIDDEN4_UNITS)
        self.fc5 = nn.Linear(HIDDEN4_UNITS, HIDDEN5_UNITS)
        self.fc6 = nn.Linear(HIDDEN5_UNITS, output_size)
        
    
    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        x = self.fc4(x)
        x = F.relu(x)
        x = self.fc5(x)
        x = F.relu(x)
        x = self.fc6(x)
        return x
