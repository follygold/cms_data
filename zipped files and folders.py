zip_divs= soup.find_all('div', attrs={'class':class_name})
zip_divs = zip_divs[3:]
folder_names = []
os.mkdir('Zip_Files')
for link in zip_links:
    res = requests.get(link)
    file_name = link.split('zip')[1].split('/')[1].split('.')[0]
    zip_name = file_name + '.zip'
    
    print('*'* 80)
    # Write zip content to file
    with open(zip_name, "wb") as code:
        code.write(res.content)
    
    folder_name = file_name.title() + '-Folder'
    print(folder_name)
    os.mkdir(folder_name)
    folder_names.append(folder_name)
    
    # opening the zip file in READ mode
    with ZipFile(zip_name, 'r') as zipped:
        # printing all the contents of the zip file
        zipped.printdir()
  
        # extracting all the files
        print('Extracting all the files now...')
        zipped.extractall(folder_name)
        print('Done!\n')
    
    # Store Zip files in a folder
    os
    shutil.move(zip_name, 'Zip_Files/{}'.format(zip_name))
