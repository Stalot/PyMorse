from icecream import ic
from datetime import datetime

class iceicebaby():
    "Configures the Icecream module"
    instance = None
    def __new__(cls):
        if cls.instance != None:
            print('WARNING: Debug cream created twice!')
        
        cls.instance = cls
        return super().__new__(cls)

    def __init__(self):
        today = datetime.today()
        log_date = today.strftime('%H:%M:%S')

        ic.enable()
        ic('Cream ready.')
        ic.configureOutput(prefix=f'{log_date} --> ', includeContext=True)