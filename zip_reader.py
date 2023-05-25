import zipfile

# Path to the password-protected zip file
zip_file_path = '1234.zip'

# Password for the zip file
password = '1234'

try:
    # Open the zip file with the given password
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Set the password for the zip file
        zip_ref.setpassword(password.encode('utf-8'))
        
        # Extract all the files from the zip file to a specified directory
        zip_ref.extractall()

    print('Zip file extracted successfully.')
    
except zipfile.BadZipFile:
    print('Invalid zip file.')

except RuntimeError:
    print('Incorrect password.')
