# mamexmlsplitter
Quick Python 3+ script to extract Neo Geo, Naomi, Atomiswave .xml's from MAME


I wrote this for my personal use after not being able to find a quick and simple way to extract a few systems out of the MAME.xml to create playlists in Retroarch. At present it will take the name of the sourcefile (e.g. naomi.cpp) search all matching machines and dump them out to a new file in the same directory as the source. Output files are named mame-xxxx.xml where xxxx is the name of the sourcefile minus the .cpp extension. Extracted .xml files are great for RetroArch, especially NAOMI and ATOMIWAVE, you can manually scan with them to create new playlists, then setup FlyCast to play them :)

An example of what a Naomi game looks like in a mame.xml:  
```
<machine name="beachspi" sourcefile="naomi.cpp" romof="naomi2">
<description>Beach Spikers (GDS-0014)\</description>
<foo bar>
<foo bar>
<foo bar>
<foo bar>
</machine>
```

To extract use the following command line:
```
python .\mamexmlsplitter.py -f 'N:\EMU\Mame\mame0242.xml' -src neogeo.cpp 
```

This will then match all naomi.cpp titles and dump the complete ```<machine>   </machine>```  entry out into the new file named mame-naomi.xml in the same dir as the input .xml file. This is based on Windows, this should work on Linux as well but let me know if not and I'll help fix that. 

This is pretty rough and ready, it will not check for the existence of an existing file (not a major issue as in theory it will always be replaced by the same or newer) and has no way at present to handle making software list for computers systems (for example ZX Spectrum +3 disks)

The script accepts the following arguments and abbreviations:
```
  -h, --help            show this help message and exit
  
  --file FILE, -f FILE  (Path to MAME.xml file, enclose in quotes if path has spaces)
  
  --sourcefile SOURCEFILE, -src SOURCEFILE (Name of system sourcefile, e.g. naomi.cpp)
  ```
  
 **Recommended -src searches:**  
  - **atomiswave.cpp** For any Atomiswave games  
  - **naomi.cpp**      For any Naomi/Naomi2 Rom only or Rom/GD games  
  - **neogeo.cpp**     For any NeoGeo games regardless of MVS/AES  
  - **neogeocd.cpp**   For any NeoGeo CD games  
 
 If you want to make combi files for example ATOMISWAVE + NAOMI, open both new .xml's in your favourite text editor and copy everything between ```<mame>   </mame>``` in one and paste before the closing ``` </mame>``` in the other and save as a new .xml (to prevent accidental overwrites). You can of course play around and use other .cpp's to create your own specialised lists.
 
 **Future plans:**
 - Try and figure out how to make software lists
 - Tidy code and add file exists check/override (either as y/n or commandline arg or both)
 - PyGUI based GUI to make it more point and click, could allow for multiple systems to be output into one file
 - Suggestions?

**License:**  
None, honestly use this code as you want, if you fork it or whatever please be kind enough to tag me as the original creator.
