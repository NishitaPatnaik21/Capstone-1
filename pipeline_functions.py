import tarfile
from pathlib import Path
from panimg import convert


def unzip_downloaded_file(fpath, expected_dir_path):
    if fpath.endswith("tar.gz"):
        tar = tarfile.open(fpath, "r:gz")
        tar.extractall(path=expected_dir_path)
        tar.close()
    elif fpath.endswith("tar"):
        tar = tarfile.open(fpath, "r:")
        tar.extractall(path=expected_dir_path)
        tar.close()
    else:
        print("Error : Incorrect file format")


"""
This function is to convert a directory of svs files to tif file

directory_name : The path where all the svs files are present 
projeted_directory_path : is where to save all the tif files with jpeg files 
"""


def save_svs_img_as_tiff(directory_name, projeted_directory_path):
    conver_to_tif = convert(
        input_directory=Path(directory_name),
        output_directory=Path(projeted_directory_path),
    )


# def save_svs_img_as_tiff(slide_filename, tile_size=4096):
#     slide_file = openslide.OpenSlide(slide_filename)
#     slide_width, slide_height = slide_file.dimensions

#     # tile_arr = []
#     slide_img = np.zeros((slide_height, slide_width, 3), np.uint8)
#     x_tile_num = int(np.floor((slide_width - 1) / tile_size)) + 1
#     y_tile_num = int(np.floor((slide_height - 1) / tile_size)) + 1
#     for iy in range(y_tile_num):
#         for ix in range(x_tile_num):
#             start_x = ix * tile_size
#             len_x = (
#                 tile_size
#                 if (ix + 1) * tile_size < slide_width
#                 else (slide_width - start_x)
#             )
#             start_y = iy * tile_size
#             len_y = (
#                 tile_size
#                 if (iy + 1) * tile_size < slide_height
#                 else (slide_height - start_y)
#             )
#             # tile_arr.append(((start_x, start_y), (len_x, len_y)))
#             cur_tile = slide_file.read_region(
#                 location=(start_x, start_y), level=0, size=(len_x, len_y)
#             )
#             slide_img[
#                 start_y : start_y + len_y, start_x : start_x + len_x, :
#             ] = np.array(cur_tile)[:, :, :3]

#     slide_savename = os.path.splitext(slide_filename)[0] + ".tif"
#     # misc.imsave(slide_savename, slide_img)
#     io.imsave(slide_savename, slide_img)


# def batch_convert_svs(slide_dir, tile_size=8192):
#     svs_list = [
#         svs_file for svs_file in os.listdir(slide_dir) if svs_file.endswith(".svs")
#     ]
#     for ind, svs_file in enumerate(svs_list):
#         print("Processing {}/{}: {}".format(ind + 1, len(svs_list), svs_file))
#         save_svs_img_as_tiff(svs_file, tile_size)


# unzip_downloaded_file(
#     "/home/manas/project/scripts/gdc_download_20221126_095632.019444.tar.gz", "./a"
# )
# save_svs_img_as_tiff("sample.svs")
