import os
import numpy as np
import skimage.io

path = '/nfs/diskstation/projects/dex-net/segmentation/datasets/pile_segmasks_01_28_18/modal_segmasks'

def bbox2(img):
    rows = np.any(img, axis=1)
    cols = np.any(img, axis=0)
    if rows.any() and cols.any():
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        return rmin, rmax, cmin, cmax
    return 0, 0, 0, 0,

for f in os.scandir(path):
    im_path = f.path
    if im_path.endswith('.png'):
        channel = skimage.io.imread(im_path)
        rmin, rmax, cmin, cmax = bbox2(channel)
        if (rmax - rmin + 1) == channel.shape[0] and (cmax - cmin + 1) == channel.shape[1]:
            print("Table", os.path.join(path, 'bg_remove_' + filename))
            os.rename(im_path, os.path.join(path, 'bg_remove_' + filename))
