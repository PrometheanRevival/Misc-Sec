from _winreg import *

specFTypes = ["\\*\\shell", "\\*\\shellex\\ContextMenuHandlers","\nContext menu fo specific filetypes and programs."]
allContext = "\\AllFileSystemObjects\\ShellEx"
folders = ["\\Directory\\shell", "\\Directory\\shellex\\ContextMenuHandlers"]
music = ["\\SystemFileAssociations\\Directory.Audio\\shell", "\\SystemFileAssociations\\Directory.Audio\\shellex\\ContextMenuHandlers"]
video = ["\\SystemFileAssociations\\Directory.Video\\shell", "\\SystemFileAssociations\Directory.Video\\shellex\\ContextMenuHandlers"]

def regprint(regset):
    print str(regset[len(regset)-1])
    for it in regset:
        print "\n"
        keyVal = it
        aKey = OpenKey(HKEY_CLASSES_ROOT, keyVal, 0, KEY_ALL_ACCESS)
        try:
            i = 0
            while True:
                asubkey = EnumKey(aKey, i)
                print("  " + asubkey)
                i += 1
        except WindowsError:
            pass


regprint(specFTypes)
