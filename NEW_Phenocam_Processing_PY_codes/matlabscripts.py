# coding=utf-8
import matlab.engine

eng = engine.start_matlab()
try:
    eng.phenomcam_correction(nargout=0)
except:
    print ("error")