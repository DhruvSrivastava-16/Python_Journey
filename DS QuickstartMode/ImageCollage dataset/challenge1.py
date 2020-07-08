# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:38:40 2020

@author: DHRUV
"""

import cv2
import numpy as np 
import matplotlib.pyplot as plt


bl=cv2.imread('bottom_left.jpg')
tl=cv2.imread('top_left.jpg')
br=cv2.imread('bottom_right.jpg')
tr=cv2.imread('top_right.jpg')

bl=cv2.resize(bl,(200,200))
tl=cv2.resize(tl,(200,200))
br=cv2.resize(br,(200,200))
tr=cv2.resize(tr,(200,200))

ls=np.vstack([bl,tl])
rs=np.vstack([br,tr])

clg_wm=np.hstack([ls,rs])
plt.imshow(clg_wm)

bordersize = 10
clg_wm = cv2.copyMakeBorder(
    clg_wm,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)]
)

cv2.imwrite('collage_pokemon.jpg',clg_wm)