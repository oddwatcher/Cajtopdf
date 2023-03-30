#!./python/bin/python3
import os
from cajparser import CAJParser as CAJ
class files:
    filelist = list()
    dirlist = list()

def recursivefind(Dir,filelist,dirlist,lastdir):
 for i in os.listdir(Dir):
        if os.path.isdir(i):
            if len(lastdir)!=0:
                recursivefind(i,filelist,dirlist,lastdir+'/'+Dir)
            else:
                recursivefind(i,filelist,dirlist,Dir)
        else:
            if not i.endswith(".pdf"):
                if not i.endswith(".html"):
                    if not i.startswith("."):
                        filelist.append(lastdir+'/'+Dir+'/'+i)
                        dirlist.append(lastdir+'/'+Dir+'/')
            
if __name__ == "__main__":
    File = files()
    dirs = input("target dir:")
    dirs=dirs.replace('\\','/')
    try:
        os.chdir(dirs)
    except:
        print(f"{dirs} not exist.")
        exit()
    recursivefind(dirs,File.filelist,File.dirlist,'')
    #print (File.filelist)
    #print (File.dirlist)
    for i,j in enumerate(File.filelist) :
        try:
            caj = CAJ(j)
            if caj.format == "PDF" or caj.format == "KDH":
                print(f"{j} is not a convertable file\n")
            else:
                output = j+".pdf"
                os.chdir(File.dirlist(i))
                caj.convert(output)
        except Exception:
            print(f"{j}is not a valid file\n")