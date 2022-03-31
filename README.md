# wowModelRipping
Tools to make it easier to rip wow models for wc3 custom maps

# Needed Programms
- WoWModelViewer
- War3ModelEditor
- blplab
- MdlVis 1.41
- CASCExplorer

# Usage
- crawlCasc.py: moves all items Exported out of CASCExplorer into current working directory
- optimize.py: detects same texture files and merges the Names of it, to safe mapspace
- removeShit.py: removes the not needed part of m2 files.
- jm2converter.jar: NOT MINE !!!, after using removeShit.py, use this on the files, so it can be opened with MdlVis
you can make a MassM2Converter.bat with this code 
```
FOR %%i IN (*.m2) DO java -jar C:\Users\<YOU>\<PathToRepo>\jm2converter.jar -in C:\Users\<YOU>\Documents\ModelsWorkspace%%i -out C:\Users\<YOU>\Documents\ModelsWorkspace%%i -bc
```
- addPrefix_TST.py: adds Prefix to files, to change Prefix, change the filename. currently Prefix is TST (i know i should burn in hell for that, but thats what corona and alcohol does)
- remPrefix: removes the added Prefix
