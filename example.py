# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 00:10:26 2022

@author: Giorgio
"""


import totec.function as tt
import numpy as np
import matplotlib.pyplot as plt

#%% 1. Open file and set page preferencies

# the txt file will be in lateX syntax, then just use it or past the text in a LateX editor


ff = open('general.txt','w+')
tt.begin(ff, title = 'Example', headL = 'header left', headR = 'header right', headC = 'El centro', footL ='foot left', footC = '\\thepage', footR = 'foot right')
tt.title(ff, title = 'Example', subtitle='An example with text and figures', author = 'gru998')

# for begin and 

tt.write(ff, 'This is the example:\nThis is the command to write text')

#%% 2. Do your calculations

xx = np.array([0,1,2,3])
yy = (xx**2)/(xx**0.5+1) + np.sqrt(xx)


#%% 3. Plot figures easily

plt.figure(1)
plt.plot(xx, yy, label = 'il test')
plt.title('Ecco il test')
plt.legend(loc = 'upper right')
plt.savefig('test.png')

#here

tt.tofig('test.png', ff, caption = 'This is how to set the caption')

#%% 4. From matrix to table

tutt = np.array([xx, yy])
colonna_uno = ['x', 'y']
riga_uno = ['what', 'case 1', 'case 2', '...3', '...4']

# you can decide to have titles or not for rows and columns

tt.totab(tutt, ff, fr = riga_uno, fc = colonna_uno, caption = 'This used to be a matrix')

tt.totab(tutt, ff,fc = colonna_uno, caption = 'No first row')

riga_uno = riga_uno[1::]

tt.totab(tutt, ff, fr = riga_uno, caption = 'No first column')

tt.totab(tutt, ff, caption = 'Nothing')



#%% 5. convert python equation into LateX syntax

tt.write(ff, 'Figure and table obtained through the following:\n(greek letters just to show off)')

tt.toeq(ff,'yy = (xx**2)/(xx**0.5*alpha+1) + np.sqrt(xx*beta**3)')

#%% 6. final comments

tt.write(ff, '\n\nFor sure some refinements are needed, anyway this is a useful tool for save some time (maybe).')

#%% 7. Close LateX and text files

tt.end(ff)
ff.close()