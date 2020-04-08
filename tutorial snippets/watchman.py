
import os
import time
import sys
Update_interval = 1
count_update = 0
def watch(files,dir):
    global count_update
    count_update+=1
    #Assumes only on file change is done at a time.
    #all files are named like 1.png, 2.png or 1.type, 2.type
    files1 = os.listdir(dir)
    def get_new_file(files,files1):
        for file in files1:
            if file not in files:
                return file 
    
    if len(files1)==len(files)-1:
        print("One file is deleted")
        def get_num(string):
            return int(''.join([i for i in string if i.isdigit()]))
        for file in sorted(files,key=get_num):
            if file not in files1:
                print(file)
                num = get_num(file)
                type_ = file.split('.')[-1]
                for i in range((num)+1,len(files)+2):
                    if os.path.isfile(os.path.join(dir,str(i)+'.'+type_)):
                        os.rename(os.path.join(dir,str(i)+'.'+type_),os.path.join(dir,str(i-1)+'.'+type_))
                return True




    elif len(files1)==len(files)+1:
        print("One file is Added")

    elif len(files)==len(files1):
        if count_update%20==0:
        
            print("No file changes")
        return False
    else:
        print("More than one file changes")
        raise ValueError("Could not proceed further. Manual watch is needed.")

    new_file = get_new_file(files,files1)
    if new_file:

        new_name = str(len(files)+1)+'.'+new_file.split('.')[-1]
        print(new_file,' is')
        print("Found a new file. Updating with new number ",new_name)
        os.rename( os.path.join(dir,new_file),os.path.join(dir,new_name))
        #files = os.listdir(dir)
        return True
    else:
        return False

def main():
    dir = 'assets'
    print("Started watching the directory ",dir)
    files = os.listdir(dir)

    while True:
        if watch(files,dir):
            files = os.listdir(dir)
        time.sleep(Update_interval)

Update_interval =  float(sys.argv[1])
print("Update interval is set to ",Update_interval)
main()