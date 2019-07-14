import cv2
import os
import pydicom
import glob

# As per my setup, input data files are in "dicom-images-test" directory at the root folder. The
# output folder is 'output_dir'. You may change the path as per your file structure.

######### Dependencies ################
# Install conda
# Create a virtual environment (https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
# Install pydicon library (https://anaconda.org/conda-forge/pydicom)
# https://pypi.org/project/opencv-python/
# Reference: https://www.kaggle.com/onealbao/dicom-to-jpeg-conversion-kernel

inputdir = 'dicom-images-test'
outdir = 'output-dir'

# get all dcm files from the test folder
def getAllFiles(path):
    dcmFiles = []
    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            if x.endswith(".dcm"):
                dcmFiles.append([dirpath, x])
    return dcmFiles

allDCMImages = getAllFiles(inputdir)

for file in allDCMImages:
    # file[0] contains path
    # file[1] contains file name
    filename = os.path.join(file[0],file[1])
    ds = pydicom.read_file(filename)  # read dicom image
    img = ds.pixel_array  # get image array

    #print(filename)
    print(outdir + "/" + file[0])
    if not os.path.exists(outdir + "/" + file[0]):
        os.makedirs(outdir + "/" + file[0])

    cv2.imwrite(outdir + "/" + filename.replace('.dcm', '.png'), img)  # write png image