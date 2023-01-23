from flask import Flask, render_template
import large_image
from PIL import Image
import slideio
import os
import numpy as np
os.add_dll_directory('C:/Users/Neha/AppData/Local/Programs/Python/Python38/lib/site-packages/openslide/openslide-win64-20221111/bin')
import openslide
from openslide.deepzoom import DeepZoomGenerator
import io
import base64
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

os.add_dll_directory('C:/Users/Neha/AppData/Local/Programs/Python/Python38/lib/site-packages/openslide/openslide-win64-20221111/bin')

wsi_path='TCGA-OL-A6VO-01A-01-TSA.1654A5EF-A6C0-47C6-BD01-56A52F368F2A.svs'
size=os.path.getsize(wsi_path)
print(size)
slide = openslide . OpenSlide ( wsi_path )
Image.MAX_IMAGE_PIXELS = None
app = Flask(__name__)

#Home Page
@app.route('/')
def index():
    return render_template('home.html')

#Sign Up Page
@app.route('/signup')
def signup():
    return "Sign Up Page"

#Sign In Page
@app.route('/signin')
def signin():
    return "Sign In Page"

@app.route('/Modal')
def modal():
    return render_template('modal.html')
    

#New Project
@app.route('/Project')
def project():
    return render_template('project.html')


@app.route('/Annotate')
def annotate():
    slide_props = slide.properties
    print(slide_props)

    print("Vendor is:", slide_props['openslide.vendor'])
    print("Pixel size of X in um is:", slide_props['openslide.mpp-x'])
    print("Pixel size of Y in um is:", slide_props['openslide.mpp-y'])

    #Objective used to capture the image
    objective = float(slide.properties[openslide.PROPERTY_NAME_OBJECTIVE_POWER])
    print("The objective power is: ", objective)

    # get slide dimensions for the level 0 - max resolution level
    slide_dims = slide.dimensions
    print(slide_dims)

    #Get a thumbnail of the image and visualize
    slide_thumb_600 = slide.get_thumbnail(size=(600, 600))
    slide_thumb_600.show()

    #Convert thumbnail to numpy array
    slide_thumb_600_np = np.array(slide_thumb_600)
    plt.figure(figsize=(8,8))
    plt.imshow(slide_thumb_600_np)    


    #  Get slide dims at each level. Remember that whole slide images store information
    #as pyramid at various levels
    dims = slide.level_dimensions

    num_levels = len(dims)
    print("Number of levels in this image are:", num_levels)

    print("Dimensions of various levels in this image are:", dims)

    #By how much are levels downsampled from the original image?
    factors = slide.level_downsamples
    print("Each level is downsampled by an amount of: ", factors)
    

    #Generate object for tiles using the DeepZoomGenerator
    tiles = DeepZoomGenerator(slide, tile_size=256, overlap=0, limit_bounds=False)
    #Here, we have divided our svs into tiles of size 256 with no overlap. 

    #The tiles object also contains data at many levels. 
    #To check the number of levels
    print("The number of levels in the tiles object are: ", tiles.level_count)

    print("The dimensions of data in each level are: ", tiles.level_dimensions)

    #Total number of tiles in the tiles object
    print("Total number of tiles = : ", tiles.tile_count)

    #How many tiles at a specific level?
    level_num = 11
    print("Tiles shape at level ", level_num, " is: ", tiles.level_tiles[level_num])
    print("This means there are ", tiles.level_tiles[level_num][0]*tiles.level_tiles[level_num][1], " total tiles in this level")

    tile_count_in_large_image = tiles.level_tiles[16] #126 x 151 (32001/256 = 126 with no overlap pixels)

    ###### Saving each tile to local directory
    cols, rows = tiles.level_tiles[11]
    print(cols,rows)
    image_urls=[]
    tile_dir = "static"
    for row in range(rows):
        for col in range(cols):
            tile_name = os.path.join(tile_dir, '%d_%d' % (col, row))
            print("Now saving tile with title: ", tile_name)
            temp_tile = tiles.get_tile(11, (col, row))
            temp_tile_RGB = temp_tile.convert('RGB')
            temp_tile_np = np.array(temp_tile_RGB)
            plt.imsave(tile_name + ".png", temp_tile_np)
            image_urls.append(tile_name+".png")

    return render_template('Annotate.html',image_urls=image_urls)
    


if __name__ == "__main__":
    app.run()