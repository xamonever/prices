from .abs_messege import AbstractMessege  

class Messege(AbstractMessege):
    """docstring for Messege"""
   
    __id = None
    __labels = None
    __snippet = None
    __from = None
    __parts_list = None
    __subject = None
    __date = None
    __attachmentIDs = None
    __attachmentName = None
    __from_head_list = ['From', 'Subject', 'Date', 'Content-Description']
    __MsgCl = '_Messege__%s'

    def __init__(self, fullMessege):
        self.__id = fullMessege['id']
        self.__labels = fullMessege['labelIds']
        self.is_marked = True if 'Label_1' in fullMessege['labelIds'] else False 
        self.__snippet = fullMessege['snippet']
        self.set_head(fullMessege['payload']['headers'])

        self.__parts_list = self.get_part_list(fullMessege['payload'])
        self.__attachment_list = self.get_file_name_attachID()
        

    def __str__(self):
        return 'From: %s, Subject: %s, \n %s' % (self.__from, self.__subject, self.__snippet)


    def get_id(self):
        return self.__id


    def get_attachment_list(self):
        if self.is_marked:
            return None
        return self.__attachment_list


    def get_head(self):
        return {self.transform_header(h): getattr(self, self.__MsgCl % self.transform_header(h)) for h in self.__from_head_list}


    def set_head(self, headers):
        for header in self.__from_head_list:
            setattr(self, self.__MsgCl % self.transform_header(header), self.get_from_headers(headers, header))


    def get_from_headers(self, headers, name):
        for header in headers:
            if header['name'] == name: return header['value']
        return None


    def transform_header(self, header):
        return header.lower().replace('-', '_')


    def get_part_list(self, payload):
        if 'parts' in payload.keys():
            return payload['parts']
        return [payload]


    def get_file_name_attachID(self):
        return [{'msgID': self.__id, 'fileName': part['filename'], 'id': part['body']['attachmentId']} for part in self.__parts_list if part['filename']]
