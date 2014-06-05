import sys,os
import prop_common
from prop_common import *

f_train = open('label_feats/train_accent.lsvm','r')
g_train = open('label_feats/train_accent_formatted.lsvm','w')


for line in f_train:
  ret = prop_common.process_accent_line(line)
  g_train.write(ret)
  g_train.write('\n')

f_train.close()
g_train.close()

f_test = open('label_feats/test_accent.lsvm','r')
g_test = open('label_feats/test_accent_formatted.lsvm','w')

for line in f_test:
  ret = prop_common.process_accent_line(line)
  g_test.write(ret)
  g_test.write('\n')

f_test.close()
g_test.close()
