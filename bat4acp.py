import subprocess
import glob
import os
def main():
    batfiles=glob.glob(r"C:\\Users\\user\\git\\windows_macro\\*.bat")
    # dirs=[f for f in files if os.path.isdir(os.path.join(base_Image, f))]
    for batfile in batfiles:
        name=os.path.splitext(os.path.basename(batfile))[0]
        path=r'C:\Users\user\anaconda3\Scripts\zzzzz.bat'
        with open(path) as f:
            s=f.read()
            print(type(s))
            print(s)    
        s=s.replace('zzzzz', name)
        path_w='C:\\Users\\user\\anaconda3\\Scripts\\'+name+'.bat'
        with open(path_w, mode='w') as f:
            f.write(s)
        with open(path_w) as f:
            print(f.read())
        # subprocess.Popen(["notepad", path_w])
if __name__ == "__main__":
    main()
