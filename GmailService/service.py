import os.path
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from .abs_factory import AbstractFactory

from .messege import Messege
from .attachment import Attachment


class Service(AbstractFactory):
    """Gmail Service Class"""
    __user_id = None
    __creds = None
    __service = None
    __labels = None
    __UM = None

    def __init__(self, token_fileName, SCOPES, user_id, credentials_fileName, app, version, labels):
        self.__user_id = user_id
        self.__labels = labels
        self.__creds = self.get_and_refresh_creds(token_fileName, SCOPES, credentials_fileName)
        self.__service = build(app, version, credentials=self.__creds)
        self.__UM = self.__service.users().messages()
        self.__UL = self.__service.users().labels()


    def __str__(self):
        return 'Service object with userID:  %s' % self.__user_id


    def get_messege(self, msg=None):
        if not msg:
            msg = self.get_messegeIDs_list()[0]
        return Messege(self.__UM.get(userId=self.__user_id, id=msg['id']).execute())


    def get_messege_list(self, msgIDs=None):
        if not msgIDs: 
            msgIDs = self.get_messegeIDs_list()
        return [Messege(self.__UM.get(userId=self.__user_id, id=msg['id']).execute()) for msg in msgIDs]


    def get_messegeIDs_list(self):
        return self.__UM.list(userId=self.__user_id, labelIds=self.__labels).execute().get('messages', [])


    def get_attachment(self, attach, save=None):
        return Attachment(attach, self.get_attachment_data(attach['msgID'], attach['id']), save=save)


    def get_attachment_data(self, msgID, attID):
        return self.__UM.attachments().get(   
                                    userId=self.__user_id, 
                                    messageId=msgID, 
                                    id=attID
                                ).execute()

    def get_and_refresh_creds(self, token_fileName, SCOPES, credentials_fileName):
        creds = None
        if os.path.exists(token_fileName):
            with open(token_fileName, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_fileName, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_fileName, 'wb') as token:
                pickle.dump(creds, token)
        return creds


    def refresh_labels(self, ms):
        msg_labels = {'removeLabelIds': [], 'addLabelIds': ['Label_1']}
        return self.__UM.modify(userId=self.__user_id, id=ms.get_id(), body=msg_labels).execute()

