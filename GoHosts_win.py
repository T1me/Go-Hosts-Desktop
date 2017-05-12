# -*- coding:gbk -*-

import urllib2
import os
import time
import shutil


version = '0.1'

def out():
    out = raw_input('\n���ᰴ��[Enter]�˳� . . .')
    exit()


print 'Go Hosts for Windows v%s' % version
print '-'*40
#  title

while 1:
    backup_option = raw_input('�Ƿ���Ҫ���ݵ�ǰhosts������[y/n]ѡ�� ')
    if backup_option == 'y'or backup_option == 'Y':
        try:
            print '����hosts�ļ�',
            usrdir = os.environ['USERPROFILE']
            backup_dir = '%s\Documents\GoHosts\\backup' % usrdir
            print '.',
            if not os.path.isdir(backup_dir):
                os.makedirs(backup_dir)
            print '.',
            hosts_path = '%s\System32\drivers\etc\hosts' % os.environ['SYSTEMROOT']         # TODO: improve
            print '.',
            backup_time = str(time.strftime('20%y%m%d%H%M%S'))
            backup_path = '%s\hosts%s' % (backup_dir, backup_time)
            shutil.copy(hosts_path, backup_path)
            print '�ɹ�'
            print '\n�����ļ�·��Ϊ\n"%s"' % backup_path
            break
        except:
            print 'ʧ��'
            print '-' * 40
            print '���ֶ�����hosts�ļ�'
            print '"C:\Windows\System32\drivers\etc\hosts"'
            out()
    elif backup_option == 'n'or backup_option == 'N':
        break
    else:
        continue
print '-'*40
#  backup

try:
    print '����hosts�ļ�',
    req = urllib2.Request('https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts')
    hosts_dl = urllib2.urlopen(req).read()
    print '.',
    f = open('hosts','wb')
    print '.',
    f.write(hosts_dl)
    print '.',
    f.close
    print '�ɹ�'
except:
    print 'ʧ��'
    print '-'*40
    print '�������������µ�ַ�ֶ�����'
    print 'https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts'
    out()
#  download hosts file

try:
    print '���ϵͳĿ¼',
    windir = os.environ['SYSTEMROOT']
    target_path = '%s\System32\drivers\etc\hosts' % windir
    print '. . . �ɹ�'
except:
    print '. . . ʧ��'
    print '-'*40
    print '���ֶ�����hosts�ļ���"C:\Windows\System32\drivers\etc\\"'
    out()
# get the target path

try:
    print '�ƶ�hosts�ļ�',
    shutil.copy('hosts', target_path)
    print '. . . �ɹ�'
    print '-'*40
    print '��װ��ɣ������ڿ������ŵط�����վ��'
    print '��ǰĿ¼�µ�hosts�ļ����ֶ�ɾ��'              # TODO: improve
except:
    print '. . . ʧ��'
    print '-'*40
    print '���Ҽ��Թ���Ա������У����ֶ�����hosts��\n"%s\System32\drivers\etc\\"' % windir
finally:
    out()
#  move hosts file