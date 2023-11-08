import sys

class customException(Exception):
    def __init__(self,error_message,error_details):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        #FROM EXE_INFO WE GET OBJECT ADDRESS FROM THAT ADDRESS WE CAN METHOD,CLASS EVERY_INFORMATION THAT"S WHY IN 
        # BELOW CODE WE USE METHOD LIKE TB_LINENO AND FILE_NAME 
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))

if __name__ == "__main__":
    try:
        
        a=1/0
    
    except Exception as e:
        raise customexception(e,sys)
        
        