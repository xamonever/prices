import os, time, psutil
from Configs.staticConfig import StaticConfig
from GmailService.service import Service
from GmailService.abs_factory import AbstractFactory
from Prices import PriceLoader, exceptions
from Ui import UI

DIRECTORY = '.\\Files\\temp'
END_DIRECTORY = '.\\Files\\downloaded'
db_name = '.\\Configs\\excel.db'


def main(service=None, loader=None, current_session=None):
    if current_session: 
        current_session.start_session()
    # mes = service.get_messege()
    # att = service.get_attachment(mes.get_attachment_list()[0], save=True)
    # format_loader = loader.create_format_loader(att.get_fileName()) 

    if loader:
        for file_name in os.listdir(DIRECTORY):
            try:
                format_loader = loader.create_format_loader(file_name) 
                format_loader.AL.run()
                    
                os.rename(os.path.join(DIRECTORY, file_name), os.path.join(END_DIRECTORY, file_name))
            except exceptions.NoFileExeption:
                pass


if __name__ == '__main__':
    print('Start...\n')
    commands = input('Enter commands: \nUI - interface, \nPR - price loader\nYour choice:  ')

    
    main(
      Service(**StaticConfig.get_credentials_conf()), 
      loader=PriceLoader(**StaticConfig.get_pl_config(), db_name=db_name, db_refresh=False) if 'PR' in commands.upper() else None,
      current_session=UI(db_name=db_name) if 'UI' in commands.upper() else None,
      )

    print('\nEND...')
    time.sleep(100)
