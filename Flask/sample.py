import os

import large_image
from PIL import Image

import os
os.add_dll_directory('C:/Users/Neha/AppData/Local/Programs/Python/Python38/lib/site-packages/openslide/openslide-win64-20221111/bin')
import openslide
import io
import base64
# %%
from IPython.display import display, Image, HTML
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# %% 

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
import sys
import large_image
for p in sys.path:
    print(p)

import os
os.add_dll_directory('C:/Users/Neha/AppData/Local/Programs/Python/Python38/lib/site-packages/openslide/openslide-win64-20221111/bin')
import openslide
wsi_path='TCGA-OL-A6VO-01A-01-TSA.1654A5EF-A6C0-47C6-BD01-56A52F368F2A.svs'
size=os.path.getsize(wsi_path)
print(size)
slide = openslide . OpenSlide ( wsi_path )
from openslide . deepzoom import DeepZoomGenerator
# Print the case-level label
def print_slide_details(slide, show_thumbnail=True, max_size=(600,400)):
    """Print some basic information about a slide"""
    # Generate a small image thumbnail
    if show_thumbnail:
        display(slide.get_thumbnail(size=max_size))
        display(HTML('<img >'))

    # Here we compute the "pixel spacing": the physical size of a pixel in the image.
    # OpenSlide gives the resolution in centimeters so we convert this to microns.
    spacing = 1  / 10000
    
    print(f"File id: {slide}")
    print(f"Dimensions: {slide.dimensions}")
    print(f"Microns per pixel / pixel spacing: {spacing:.3f}")
    print(f"Number of levels in the image: {slide.level_count}")
    print(f"Downsample factor per level: {slide.level_downsamples}")
    print(f"Dimensions of levels: {slide.level_dimensions}")

biopsy = openslide.OpenSlide(wsi_path)
print_slide_details(biopsy)
biopsy.close()
    
