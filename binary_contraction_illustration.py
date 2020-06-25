#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 19:22:36 2020

@author: vk17590
"""

def quadrant(point):
    """
    Function returning the quadrant a point belongs to.
    """
    return 0

def binary_contraction_step(points, points_q):
    """
    Step in binary contraction procedure
    """
    
    new_points=points
    for i in range(4):
        
        middle_point = 0.5*points[0]+0.5*points[1]
        middle_point_q = quadrant(middle_point)
        
        if middle_point_q == points_q[0]:
            new_points[0] = middle_point
            return new_points[[1,2,3,0]], points_q[[1,2,3,0]]
        
        if middle_point_q == points_q[1]:
            new_points[1] = middle_point
            return new_points[[1,2,3,0]], points_q[[1,2,3,0]]
        
        new_points = new_points[[1,2,3,0]]
    return points, points_q

if __name__ == '__main__':

    points = [] #input points
    points_q = quadrant(points)

    for i in range(100):
        new_points, new_points_q = binary_contraction_step(points, points_q)
        if (new_points == points).all():           
            break
        points = new_points
        points_q = new_points_q
    average=0.25*(points[0]+points[1]+points[2]+points[3])