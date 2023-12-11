import numpy as np
# from assets import student
# from assets import studentencodes, teacherencodes

def loadteacherencodes():
    encodesaves = np.loadtxt('all_encoding.txt', delimiter=',')    
    return encodesaves
def loadstudentencodes():
    encodesaves = np.loadtxt('studentencodes.txt', delimiter=',')    
    return encodesaves

    a = loadstudentencodes()