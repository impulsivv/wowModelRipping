import glob
import os

def getSkin(name):
        skin_file = file.split(".")
        skin_file[1] += "00"
        skin_file[-1] = ".skin"
        return skin_file

root_path = ".\\"
get_filename = lambda x: x.split(".")[1].split("\\")[-1]
name_list = list(map(get_filename
                    ,glob.glob(root_path + '*.obj')))
print(name_list)
cnt = 0
moved=set()
for file in glob.glob(root_path + '**\\*.m2', recursive=True):
    decisionList = [i for i in name_list if(i in file)]
    for i in decisionList: moved.add(i)
    if any(decisionList):
        os.rename(file, root_path + get_filename(file) + ".m2")
        skin_file = getSkin(file)
        os.rename(skin_file, root_path + get_filename(skin_file) + ".skin")
        cnt += 1

        
        
print("Moved {} m2 and skin files".format(cnt))
print("missed {}".format(set(name_list) - moved)