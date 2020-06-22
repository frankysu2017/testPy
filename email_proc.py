#!/usr/bin/env python3
# coding=utf-8
# email_init.py

import email
import re
import os
import shutil
import chardet
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil.parser import parse
import multiprocessing
#from docx import Document
#import win32com
#import win32com.client
#import xlrd, openpyxl
#wc = win32com.client.constants


def get_subject(msg):
    s = msg.get('subject')
    if s:
        s_decoded = email.header.decode_header(s)
        if isinstance(s_decoded[0][0], bytes):
            return s_decoded[0][0].decode(s_decoded[0][1], 'ignore')
        else:
            return s_decoded[0][0]
    else:
        return None


def get_sendtime(msg):
    if 'date' in msg:
        return parse(msg.get('date'))
    else:
        return None


def get_sender(msg):
    sname, send_box = email.utils.parseaddr(msg.get('from'))
    if sname:
        sname = email.header.decode_header(sname)
        if isinstance(sname[0][0], bytes):
            send_name = sname[0][0].decode(sname[0][1], 'ignore')
        else:
            send_name = sname[0][0]
    else:
        send_name = None
    return send_name, send_box


def get_receiver(msg):
    rname, receive_box = email.utils.parseaddr(msg.get('to'))
    if rname:
        rname = email.header.decode_header(rname)
        if isinstance(rname[0][0], bytes):
            receive_name = rname[0][0].decode(rname[0][1], 'ignore')
        else:
            receive_name = rname[0][0]
    else:
        receive_name = rname
    return receive_name, receive_box


def get_mainbody(msg):
    mainbody = ''
    if msg.get_payload(decode=True) and msg.get_content_charset():
        mainbody = msg.get_payload(decode=True).strip().decode(msg.get_content_charset(), 'ignore')
        html_flag = re.search('text/(.*)', msg.get_content_type()).group(1).lower()
        if html_flag == 'html':
            if '<html' in mainbody:
                prefix, html_text, suffix = re.search('(.*)(<html.*</html>)(.*)', mainbody, re.DOTALL+re.IGNORECASE).groups()
                html_text = BeautifulSoup(html_text, features="html.parser").body.get_text()
                mainbody = prefix + '\n' + html_text + '\n' + suffix
    mainbody = re.sub('[\n]+', '\n', mainbody)
    return mainbody


def get_attachment(msg, mail_address):
    attachment_name = msg.get_filename()
    if attachment_name:
        attachment_name = email.header.decode_header(attachment_name)
        if isinstance(attachment_name[0][0], bytes):
            attachment_name = attachment_name[0][0].decode(attachment_name[0][1], 'ignore')
        else:
            attachment_name = attachment_name[0][0]
        if '\\' in attachment_name:
            attachment_name = attachment_name.replace('\\', '_').replace(':', '')

        attachment_content = msg.get_payload(decode=True).strip()
        path = 'C:\\Download\\attachments\\' + mail_address.replace('.', '_')
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + '\\' + attachment_name, 'wb') as f:
            f.write(attachment_content)
        return attachment_name, ''


def email_init(emlfile):
    email_name = emlfile.split('/')[-1].replace('.', '_')
    ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
    mail_address = emlfile.split('/')[-1].split('_')[0]
    encode = chardet.detect(open(emlfile, 'rb').read())['encoding']
    with open(emlfile, 'r', encoding=encode) as eml:
        msg = email.message_from_file(eml)
        subject = get_subject(msg)
        subject = ILLEGAL_CHARACTERS_RE.sub(r'', subject)
        send_time = get_sendtime(msg)
        send_name, send_box = get_sender(msg)
        send_name = ILLEGAL_CHARACTERS_RE.sub(r'', send_name)
        send_box = ILLEGAL_CHARACTERS_RE.sub(r'', send_box)
        receive_name, receive_box = get_receiver(msg)
        receive_name = ILLEGAL_CHARACTERS_RE.sub(r'', receive_name)
        receive_box = ILLEGAL_CHARACTERS_RE.sub(r'', receive_box)
        attachment_file, attachment_text = '', ''
        attachment_file_temp, attachment_text_temp = '', ''
        if msg.is_multipart():
            mail_content = ''
            for part in msg.get_payload():
                if part.get_content_maintype() == 'multipart':
                    part_content = ''
                    for subpart in part.get_payload():
                        subpart_content = get_mainbody(subpart)
                        part_content += subpart_content
                elif part.get_content_maintype() == 'text':
                    part_content = get_mainbody(part)
                elif part.get_content_maintype() == 'application':
                    part_content = ''
                    attachment_file_temp, attachment_text_temp = get_attachment(part, mail_address)
                else:
                    part_content = ''
                    attachment_file_temp, attachment_text_temp = get_attachment(part, mail_address)
                attachment_file = attachment_file_temp + '\n' + attachment_file
                attachment_text = attachment_text_temp + '\n' + attachment_text
                mail_content += part_content
        else:
            mail_content = get_mainbody(msg)
        mail_content = ILLEGAL_CHARACTERS_RE.sub(r'', mail_content)
        with open(r'C:\Download\mailbody\{}'.format(email_name), 'w', encoding='utf8') as f_mailbody:
            f_mailbody.write(mail_content)
        with open('C:\Download\mailhead\{}'.format(email_name), 'w', encoding='utf8') as f_head:
            head_str = ','.join([send_box, send_name, receive_box, receive_name, subject, str(send_time)])
            f_head.write(head_str)

        return send_name, send_box, receive_name, receive_box, str(send_time), subject, mail_content, attachment_file, attachment_text


if __name__ == '__main__':
    pool = multiprocessing.Pool(7)
    lst = os.listdir(r'C:\Download\email/')
    l2 = map(lambda x: r'C:\Download\email/{}'.format(x), lst)
    pool.map(email_init, l2)
