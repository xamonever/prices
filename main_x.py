import os, time, sys, datetime
from Configs.staticConfig import StaticConfig
from GmailService.service import Service
from Prices import PriceLoader, exceptions
from Ui import UI

DIRECTORY = '.\\Files\\today_shit'
TIMER = 30
LOOPS = 10
# db_name = '.\\Configs\\excel.db'


def main(service=None, loader=None, current_session=None):

    if current_session: 
        current_session.start_session()

    if service:
        mess = service.get_messege_list()[:3]
        for ms in mess:
            att_list = ms.get_attachment_list()
            if att_list:
                att = service.get_attachment(att_list[0], save=True)
                att.check_and_save()
                service.refresh_labels(ms)

    if loader:
        for file_name in os.listdir(DIRECTORY):
            try:
                format_loader = loader.create_format_loader(file_name) 
                format_loader.run()
                    
            except exceptions.NoFileExeption:
                pass


if __name__ == '__main__':
    print('Start...\n')
    commands = input('Enter commands: \nUI - interface, \nMES - load messages, \nPR - price loader, \nLP - autonomious working, \nQ - quit... \nYour choice:  ')
    commands = commands.upper()

    now = datetime.datetime.now()
    sys.stdout = open('Configs/logs/logs %s.txt' % now.strftime("(%m) %d"), 'a')
    print('='*45, '\n', now.strftime("(%m) %d day: %H.%M"), f'({commands})')

    while True:
        main(
          service=Service(**StaticConfig.get_credentials_conf()) if 'MES' in commands else None, 
          loader=PriceLoader(**StaticConfig.get_pl_config(), db_name=None, db_refresh=False) if 'PR' in commands else None,
          current_session=UI(db_name=None) if 'UI' in commands else None,
          )
        
        if 'LP' in commands and 'PR' in commands and LOOPS:
            LOOPS -= 1
        else:
            break
    
    