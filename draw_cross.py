# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:57:48 2022

@author: talha
"""

def draw_cross(img, center_pt, size, clr=(255,0,0), thickness=3):
    '''
    Draws a cross on image with center at 'center_pt' , having length 2*size.
    Parameters
    ----------
    img : input RGB image. 
    center_pt : x and y coordinates of the center of the cross. [tuple: int]
    size : length of the cross, [ int]
    clr : color of the cross. The default is (255,0,0).
    thickness : thickness of line. The default is 3.
    '''
    x, y = center_pt
    cv2.line(img, (x-size, y-size), (x+size, y+size), clr, thickness)
    cv2.line(img, (x-size, y+size), (x+size, y-size), clr, thickness)
    
    return img
