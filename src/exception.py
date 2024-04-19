import logging
import sys

def error_message_detail(error):
    exc_type, exc_value, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message[{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error):
        error_message = error_message_detail(error)
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e)
