import pyzipper
import itertools#tomake all modules work like generator and wont stop the permutations because of lower memory
import threading
import sys


#inputs and validations
max_combination_characters = 8#maximum charcters allowed for a password
zip_file_path = "6di.zip"#input("enter file location : ")
digits = int(input("enter the length of your password :"))
bullets = list(range(0,int('9'*digits)+1))#number of combinations in a thread,i.e 8
total_elements=len(bullets)//max_combination_characters#total combination in a part
output_path = zip_file_path[0:zip_file_path.find(".")]

if digits>max_combination_characters:
    sys.exit(f"Maximum {max_combination_characters} digits for now.\nThank you!!")

#status bar
def update_status_bar(progress, total, bar_length=70):
    filled_length = int(bar_length * progress / total)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    percent = (progress / total) * 100
    sys.stdout.write(f'\r[{bar}] {percent:.1f}%')
    sys.stdout.flush()


def unzip_password_protected_file(zip_file_path, output_path, password):
    try:
        with pyzipper.AESZipFile(zip_file_path) as zf:
            zf.setpassword(password)
            zf.extractall(output_path)
        print(f"\nPassword extracted!! \nPassword :{password.decode('utf-8')}")
        return True
    except Exception as E:
        # print(str(E))
        #print(f"attempt failed :{password.decode('utf-8')}")
        return False

#**Number bruting**
#bruting passwords upto max_combination_characters characters
def number_combos(parts:list):
    zip_hit_count=0
    for password in parts:
        update_status_bar(zip_hit_count,total_elements)
        crack_status=unzip_password_protected_file(zip_file_path, output_path, str(password).encode("utf-8"))#joining iterable
        zip_hit_count+=1
    return None

#splitting to passwords into 8 equal parts
start=0
end=total_elements
combinations=[]
print("Generating password combinations ..")
for i in range(1,max_combination_characters+1):#8parts #needs optimization
    combinations.append(bullets[start:end])
    start=start+end
    end=start-end
    start=start-end
    end=start+total_elements
    if i==max_combination_characters:#remianing coombinations
        combinations.append(bullets[start:])

#intializing threads
threads=[]
print("Please wait for Execution to complete ...")
for parts in combinations:
    thread = threading.Thread(name=f"Part-{len(threads)+1}",daemon=True,target=number_combos,args=(parts,))
    threads.append(thread)
    thread.start()
# listing threads
# print(*threads,sep="\n")

# Wait for all threads to finish peacefully
for thread in threads:
    thread.join()

