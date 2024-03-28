import logging
import sys

def error_message_details(error, error_detail:sys):
    _,_, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name {0} line number {1} error message {2}".format(
        file_name, exec_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_msg = error_message_details(error_msg, error_detail=error_detail)

    
    def __str__(self):
        return self.error_msg
    

if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("divide by zero error")
        raise CustomException(e, sys)

    