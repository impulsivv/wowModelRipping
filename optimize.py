import glob
import os

def makePrePostFix(name):
    pre=[i for i in name_list if(name.startswith(i))][0]
    post=name[len(pre)+1:]
    return pre, post

root_path = ".\\"
get_filename = lambda x: x.split(".")[1].split("\\")[-1]
name_list = list(map(get_filename
                ,glob.glob(root_path + '*.mdx')))#, recursive=True)
print(name_list)

for texture in glob.glob(root_path + '*.blp'):
    if not os.path.isfile(texture): continue
    #filename = 
    pre, post = makePrePostFix(get_filename(texture))
    print("Pre: {}, Post: {}".format(pre, post))
    for cmp in glob.glob(root_path + '*.blp'):
        if (texture != cmp):
            cmp_pre, cmp_post = makePrePostFix(get_filename(cmp))
            if (post == cmp_post):
                print("{} != {}".format(texture,cmp))
                pre += "_"+cmp_pre 
                print("del {}".format(cmp))
                os.remove(cmp)
    
    filename = root_path + pre + "_" + post + ".blp"
    print("rename {} to {}".format(texture,filename))
    os.rename(texture,filename)
    
    