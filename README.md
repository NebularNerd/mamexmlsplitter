# mamexmlsplitter
Quick Python script to extract Neo Geo, Naomi, Atomiswave .xml's from MAME


I wrote this more for my personal use after not being able to find a quick and simple way to extract a few systems out of the MAME.xml to create playlists in Retroarch. At present it will take the name of the sourcefile (e.g. naomi.cpp) search all matching machines and dump them out to a new file in the same directory as the source. Output files are name mame-xxxx.xml where xxxx is the name of the sourcefile minus the .cpp extension.

This is pretty rough and ready, it wil not check for the existence of an existing file (not a major issue as in theory it will always be replaced by the saem or newer) and has no way at present to handle making software list for computers systems (for example Zx Spectrum +3 disks)

Optional arguments:

  -h, --help            show this help message and exit
  
  --file FILE, -f FILE  (Path to MAME.xml file, enclose in quotes if path has spaces)
  
  --sourcefile SOURCEFILE, -src SOURCEFILE (Name of system sourcefile, e.g. naomi.cpp)
  
 
