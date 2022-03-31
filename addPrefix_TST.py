import glob
import os
import sys

get_filename = lambda x: x.split(".")[1].split("\\")[-1]
root_path = ".\\"
file_exts = [".blp",".m2",".mdx"]
prefix = "Doodad_" + sys.argv[0].split(".")[0].split("_")[-1] + "_"
print(sys.argv[0].split(".")[0].split("_")[-1])
for file_ext in file_exts:
    for texture in glob.glob(root_path + "*" + file_ext):
        if not os.path.isfile(texture): continue
        filename = get_filename(texture)
        if not filename.startswith("Doodad"):
            os.rename(texture,prefix + filename + file_ext )
        else:
            print("{} haves allready Doodad prefix".format(texture))
