
import glob

from pdf2image import convert_from_path,convert_from_bytes
import uuid

pdf_path=''
image_path=''

count=0
for file in enumerate(glob.glob(pdf_path+'*.pdf')):
    #print(file)
    pdf_name=file[1]
    print(pdf_name)
    images=[]
    convert_from_path(pdf_name, output_folder='', fmt='jpg',thread_count=2,output_file=str(uuid.uuid4()))
