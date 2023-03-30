#!./python/bin/python3
import os
from cajparser import CAJParser as CAJ
class files:
    filelist = list()
    dirlist = list()

def absrecursivefind(Dir,filelist,dirlist):
 for i in os.listdir(Dir):
        if os.path.isdir(i):
            absrecursivefind(Dir+'/'+i,filelist,dirlist)
        else:
            if not i.endswith(".pdf"):
                if not i.endswith(".html"):
                    if not i.startswith("."):
                        filelist.append(Dir+'/'+i)
                        dirlist.append(Dir+'/')
            
if __name__ == "__main__":
    File = files()
    dirs = input("target dir:")
    dirs=dirs.replace('\\','/')
    try:
        os.chdir(dirs)
    except:
        print(f"{dirs} not exist.")
        exit()
    absrecursivefind(dirs,File.filelist,File.dirlist)
    print (File.filelist)
    print (File.dirlist)
    for i,j in enumerate(File.filelist) :
        try:
            print(f'testing file {j}\n')
            caj = CAJ(j)
        except Exception:
            print(j+' is not accecptable\n')
        else:
                os.chdir(File.dirlist[i])
                print(f'switch to working dir {File.dirlist[i]}')
                if caj.format == "KDH":
                    print(f"{j} is not a convertable file\n")
                elif caj.format == "PDF":
                    os.rename(j,j.replace('.caj','')+'pdf')
                else:
                    try:
                        output = j+".pdf"
                        
                        caj.convert(output)
                    except Exception:
                        print(f"{j} is not a valid file\n")