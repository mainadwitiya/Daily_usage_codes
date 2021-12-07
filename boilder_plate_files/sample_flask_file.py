#initializing logger
import os
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("API.log")
formatter = logging.Formatter('%(asctime)s :: %(module)s :: %(levelname)s :: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#------------------------------------------------------------------------------------------------------------------------------------------

def logger_output(message,level=2):
   
    if level==1:
        logger.info(message)
    elif level==2:
        logger.info(message)
    elif level==3:
        logger.exception(message)

    return
#------------------------------------------------------------------------------------------------------------------------------------------

try:
    import re
    import operator
    import subprocess
    import glob
    import json
    from flask import Flask,jsonify,Response,request
except:
    logger_output("Could not import the following package",level=3)
    exit(1)

app = Flask(__name__)

try:
    with open('app_config.json') as json_file:
        configuration = json.load(json_file)
        model_name_dir=configuration["model_dir"]
except:    
    logger_output("app_config.json not found",level=3)
    exit(1)



#route 1
try:        
    @app.route('/method_name', methods=["POST"]) #allow  POST requests
    def example():


        response = []
        obj = {}
        if request.method == 'POST':  #this block is only entered when the form is submitted
            request_dict = request.get_json()
            #declare the varibales accordingly and run the model  


            
       
        return obj    
           
except:
    logger_output("API failed",level=3)
    exit(1)

#------------------------------------------------------------------------------------------------------------------------------------------
   
if __name__ == '__main__':
   
   # app.run(host = '0.0.0.0',port='8004')
    serve(app, host='0.0.0.0')

#------------------------------------------------------------------------------------------------------------------------------------------
