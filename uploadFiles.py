import dropbox
import os
class Transferdata:
    def __init__(self,accesstoken) :
        self.accesstoken=accesstoken
    
    def upload_file(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        for root,dirs,files in os.walk(filefrom):
            relative_path=os.path.relpath(local_path,filefrom)
            dropbox_path=os.path.join(fileto,relative_path)
            with open(local_path,'rb') as f:
                dbx.filesupload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
def main():
    accesstoken="sl.BLd_CNySzlaXGz3h40eS7QTpak83vBnzHiQAAIX_aJ6kwiZ4NwcPUcrz-wtDfDHh1vgGmES66rJDdirQy7XuVxnGoqWnSNN-Q-vFSBD-CcO5NerWC3KS2Zytee3kQUXE2DCpNM4"
    transferdata=Transferdata(accesstoken)

    filefrom=input("enter the file path to transfer")
    fileto=input("enter the path to upload the dropbox")
    transferdata.upload_file(filefrom,fileto)
    print("file has been moved")

main()