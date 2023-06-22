import pyzipper
import multiprocessing
import sys


zip_file_path = "01234.zip"
output_path = zip_file_path[0:zip_file_path.find(".")]

def unzip_password_protected_file(zip_file_path:str, output_path:str, password)->bool:
    try:
        with pyzipper.AESZipFile(zip_file_path) as zf:
            print("HERE")
            zf.setpassword(password)
            zf.extractall(output_path)
        print(f"\nPassword extracted!! \nPassword :{password.decode('utf-8')} \nStopping threads peacefully")
        return True
    except Exception as E:
        print(str(E))
        return False

if __name__ =='__main__':
    
    #create proces based on number of cores
    process_dict={}
    num_processes = multiprocessing.cpu_count()
    for start in range(0,num_processes):
        process_dict['process-'+str(start)] = multiprocessing.Process(target=unzip_password_protected_file,args=(zip_file_path,output_path,'01234'.encode('utf-8')))
        process_dict['process-'+str(start)].start()
    
    #waiting for the process to be over
    for stop in range(0,num_processes):
        process_dict['process-'+str(stop)].join()

# unzip_password_protected_file(zip_file_path,output_path,'01234'.encode('utf-8'))

