import glob
import os
get_filename = lambda x: x.split(".")[1].split("\\")[-1]
root_path = ".\\"
file_exts = [".blp",".mdx"]

for file_ext in file_exts:
    for texture in glob.glob(root_path + "*" + file_ext):
        if not os.path.isfile(texture): continue
        filename = get_filename(texture)
        if filename.startswith("Doodad"):
            os.rename(texture,filename.split("_",2)[2] + file_ext)
        else:
            print("{} haves allready Doodad prefix".format(texture))
