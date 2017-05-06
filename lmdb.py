import os
import numpy as np
main_path = r'/home/fpsandnoob/image_output/'
class_name = os.listdir(r'/home/fpsandnoob/image_output/')
class_dict = {}
for i in range(len(class_name)):
    class_dict[class_name[i]] = i
_data = []
_label = []
data = []
label = []


for dir_path in class_name:
    p = os.listdir(main_path + dir_path)
    i = class_dict[dir_path]
    for im in p:
        _data.append(os.path.join(main_path, dir_path, im))
        _label.append(i)
num_examples = len(_label)
perm = np.arange(num_examples)
np.random.shuffle(perm)
for i in perm:
    data.append(_data[i])
    label.append(_label[i])
test_data = data[-200:]
test_label = label[-200:]
train_data = data[:-200]
train_label = label[:-200]
with open('testlist.txt', 'w+') as f:
    for i in xrange(len(test_label)):
        f.write(test_data[i])
        f.write(' ')
        f.write(str(test_label[i]))
        f.write('\n')

with open('trainlist.txt', 'w+') as f:
    for i in xrange(len(train_data)):
        f.write(train_data[i])
        f.write(' ')
        f.write(str(train_label[i]))
        f.write('\n')

with open('varlist.txt', 'w+') as f:
    for i in xrange(196):
        f.write
