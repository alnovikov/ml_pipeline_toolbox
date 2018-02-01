'''
What?
    Import csv file and transform it into a numpy array, then divide into train-test files using specified split
    randomly shuffling the data
'''

from __future__ import print_function
import numpy as np
import csv

with open('filename.csv', 'r') as csvfile:
    next(csvfile, None) #skip the first line
    data = list(csv.reader(csvfile, delimiter=","))

data_np = np.array(data,dtype=np.float32)

#example of 2-dimensional slicing of Y (where -1 - last column)
print(data_np[:,-1])

# define a function to randomly split train and test given share of the train data:
def train_test_split(data_in, train_share=0.8):
    #shuffle the data first
    np.random.shuffle(data_in)
    #defining splitting point (deduction of modulo is used for rounding down)
    split = int(train_share*(data_in.shape[0] - data_in.shape[0] % 1))
    train,test = data_in[:split],data_in[split:]
    print("Training data has %i rows.\nTest data has %i rows" % (train.shape[0],test.shape[0]))
    return(train,test)

train, test = train_test_split(data_np)
# split X and y
X_train,y_train = train[:,:-1],train[:,-1]
X_test,y_test = test[:,:-1],test[:,-1]

#check that labels contain only 1 and 0:
np.unique(y_train),np.unique(y_test)
