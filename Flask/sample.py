# %% 
import os
from PIL import Image as IMG
from PIL import  ImageDraw, ImageTk
import tkinter as tk
import os

os.add_dll_directory('C:/Users/Neha/AppData/Local/Programs/Python/Python38/lib/site-packages/openslide/openslide-win64-20221111/bin')

import openslide
#os.add_dll_directory('C:/Users/Neha/AppData/Local/Programs/Python/Python38/Lib/site-packages/vips-dev-8.14/bin')
#import pyvips
# %%
from IPython.display import display, Image, HTML
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import large_image
from pathlib import Path
from panimg import convert


# %% 





# %% 

result = convert(
    input_directory=Path("C:/Users/Neha/OneDrive/Desktop/Flask/static/input_folder"),
    output_directory=Path("/static/output_tiff"),
    
)
# %% 



# %% 



# %% 

app = tk.Tk()
# Print the case-level label
image = IMG.open("static/0_0.png")
canvas = tk.Canvas(app, width=image.width, height=image.height)
canvas.pack()
canvas.pack(anchor='nw', fill='both', expand=1)

#image = image.resize((400,400), IMG.ANTIALIAS)
image = ImageTk.PhotoImage(image)
canvas.create_image((0,0), image=image, anchor='nw')



def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), 
                      fill='red', 
                      width=2)
    lasx, lasy = event.x, event.y





  


canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)



app.mainloop()
#%%

wsi_path='TCGA-OL-A6VO-01A-01-TSA.1654A5EF-A6C0-47C6-BD01-56A52F368F2A.svs'
size=os.path.getsize(wsi_path)
print(size)

slide = openslide.open_slide(wsi_path)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
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
    

# %%
