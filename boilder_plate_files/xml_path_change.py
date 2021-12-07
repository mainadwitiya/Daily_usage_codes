import os
import xml.etree.ElementTree as ET
import glob
xml_path=''
image_path=''
#print(image_path)
file_lists=glob.glob(xml_path+'*.xml')
#print(file_lists)
image_lists=glob.glob(image_path+'*.jpg')
#print(image_lists)
count=0
for file in file_lists:
    #print(file)
    new_name=os.path.basename(file)[:-4]
    print(new_name)
    count+=1
    tree=ET.parse(file)
    root = tree.getroot()
    #print(root)
    for child in root:
        #print(child.tag)
        #print(child.text)
        if child.tag=='filename':
            image_name=child.text.split('.')
            print(image_name)
            child.text=new_name+'.jpg'
            print(child.text)
        if child.tag=='path':
            to_set_path=os.getcwd()
            #print(to_set_path)
            child.text=image_path+new_name+'.jpg'
    tree.write(file)
print(count)
