import glob, os
def removeShit(fname):
  with open(fname, 'r',encoding="ascii", errors="surrogateescape",newline="\n") as f:
    data = f.read()

  arr = list(data)
  i=0
  match=[]
  for char in arr:
    try:
      if char == "M":
        match.append(char)
      if char == "D":
        match.append(char)
      if char == "2":
        match.append(char)
      if char == "0":
        match.append(char)
    except:
      print("shithappensbutissssaaaaakniffeeee")
    finally:
      if "MD20" in "".join(match):
        break
      i+=1

  newarr = data[i-3:]

  with open(fname, 'w',encoding="ascii", errors="surrogateescape",newline="\n") as f:
      f.write("".join(newarr))


os.chdir("./")
for file in glob.glob("*.m2"):
    print(file)
    removeShit(file)
