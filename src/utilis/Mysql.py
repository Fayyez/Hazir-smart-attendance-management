import numpy as np
# from assets import student
# from assets import studentencodes, teacherencodes
import json

def loadteacherencodes():
    encodesaves = np.loadtxt('teacherencodes.txt', delimiter=',')    
    return encodesaves
def loadstudentencodes():
    encodesaves = np.loadtxt('studentencodes.txt', delimiter=',')    
    return encodesaves