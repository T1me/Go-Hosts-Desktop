# -*- coding:gbk -*-

import urllib2
import os
import time
import shutil


version = '0.2'

global backup_dir
global hosts_dir
global hosts_path

def quit_():
    raw_input('\n���ᰴ��[Enter]�˳� . . .')
    exit()

def check_environment():
    print u'���ڼ��ϵͳ����',
    try:
        backup_dir = '%s\Documents\GoHosts\\backup' % os.environ['USERPROFILE']
    except:
        backup_dir = False
    try:
        hosts_dir = '%s\System32\drivers\etc' % os.environ['SYSTEMROOT']
    except:
        hosts_dir = False
    if backup_dir and hosts_dir == False:
        print u'. . . ʧ��'
        quit_()
    else:
        print u'. . . �ɹ�'
        return backup_dir, hosts_dir

def back():
    raw_input('\n���ᰴ��[Enter]�������˵� . . .')
    main_menu()

def get_time():
    timef = str(time.strftime('20%y%m%d%H%M%S'))
    return timef

def backup():
    try:
        print u'����hosts�ļ�',
        if not os.path.isdir(backup_dir):
            os.makedirs(backup_dir)
        backup_time = get_time()
        backup_path = '%s\hosts%s' % (backup_dir, backup_time)
        shutil.copy(hosts_path, backup_path)
        print u'. . . �ɹ�'
        print u'�����ļ�·��Ϊ'
        print backup_path
    except:
        print u'. . . ʧ��'
        print u'���ֶ�����hosts�ļ�'
        print '%s\hosts' % hosts_dir
        back()

def download():
    try:
        print u'����hosts�ļ�',
        req = urllib2.Request('https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts')
        hosts_dl = urllib2.urlopen(req).read()
        print '.',
        f = open('hosts', 'wb')
        print '.',
        f.write(hosts_dl)
        print '.',
        f.close
        print u'�ɹ�'
    except:
        print u'ʧ��'
        print u'�������������µ�ַ�ֶ�����'
        print 'https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts'
        back()

def install():
    try:
        print u'��װhosts�ļ�',
        if not os.path.isfile('hosts'):
            print u'. . . �Ҳ����ļ�'
            back()
        shutil.copy('hosts', hosts_dir)
        print u'. . . �ɹ�'
        print u'��װ��ɣ������ڿ������ŵط�����վ��'
        print u'��ǰĿ¼�µ�hosts�ļ����ֶ�ɾ��'                                         #  TODO: improve
    except:
        print u'. . . ʧ��'
        print u'���Ҽ��Թ���Ա������У����ֶ�����hosts��'
        print '%s/hosts' % hosts_dir
        back()

def auto():
    os.system('cls')
    print u'------------------- �Զ��� ---------------------'
    print
    while True:
        backup_option = raw_input('�Ƿ���Ҫ���ݵ�ǰhosts������[y/n]ѡ�� ')
        if backup_option == 'y'or backup_option == 'Y':
            backup()
            break
        elif backup_option == 'n' or backup_option == 'N':
            print u'hostsδ����'
            break
        else:
            continue
    print '-------------------------------------------------'
    download()
    install()
    back()

def restore():
    global backup_dict
    backup_dict = {}
    os.system('cls')
    print u'------------------- ��ԭ���� --------------------'
    if os.path.isdir(backup_dir):
        n = 1
        for i in os.listdir(backup_dir):
            backup_dict[str(n)] = i
            n += 1
        if backup_dict:
            for k in range(1,len(backup_dict)+1):
                print
                print str(k) + '. ' + backup_dict[str(k)]
        else:
            print
            print u'���ޱ����ļ���'
    else:
        print
        print u'������Ŀ¼�����ڣ�'
    print
    print '-------------------------------------------------'
    restore_option = raw_input('��ԭ������hosts�ļ�[���]������������[n] ')
    if restore_option == 'n' or restore_option == 'N':
        backup_mgr()
    elif backup_dict:
        if restore_option in backup_dict:
            restore_path = '%s\%s' % (backup_dir, backup_dict[restore_option])
            try:
                print u'��ԭhosts����',
                shutil.copy(restore_path, hosts_path)
                print u'. . . �ɹ�'
            except:
                print u'. . . ʧ��'
            finally:
                back()
    else:
        restore()

def backup_mgr():
    os.system('cls')
    print u'------------------- ���ݹ��� --------------------'
    print
    print u'1. ���ݵ�ǰhosts�ļ�'
    print
    print u'2. ��ԭ����'
    print
    print u'3. �������˵�'
    print
    if os.path.isdir(backup_dir):
        print u'4. �򿪱���Ŀ¼'
        print
    print '-------------------------------------------------'
    option = raw_input('����[���]ѡ�� ')
    if option == '1':
        backup()
        back()
    elif option == '2':
        restore()
    elif option == '3':
        main_menu()
    elif option == '4' and os.path.isdir(backup_dir):
        os.startfile(backup_dir)
        backup_mgr()
    else:
        backup_mgr()

def option_download():
    os.system('cls')
    print u'----------------- ����hosts�ļ� -----------------'
    print
    download()
    print u'hosts�ļ������ص���ǰĿ¼'
    back()

def option_install():
    os.system('cls')
    print u'----------------- ��װhosts�ļ� -----------------'
    print
    while True:
        install_option = raw_input('ȷ����װ��ǰĿ¼�µ�hosts�ļ�������[y/n]ѡ�� ')
        if install_option == 'y'or install_option == 'Y':
            install()
            back()
        elif install_option == 'n' or install_option == 'N':
            main_menu()
        else:
            continue
    back()

def main_menu():
    os.system('cls')
    print '=========== Go Hosts for Windows v%s ============' % version
    print
    print u'1. �Զ��򵼣��򵥣�'
    print
    print u'2. ���ݹ���'
    print
    print u'3. ����hosts�ļ�'
    print
    print u'4. ��װhosts�ļ�'
    print
    print u'5. �˳�'
    print
    print '=================================================='
    option = raw_input('����[���]ѡ�� ')                                             #  TODO��raw_input(unicode) CMD exit
    if option == '1':
        auto()
    elif option == '2':
        backup_mgr()
    elif option == '3':
        option_download()
    elif option == '4':
        option_install()
    elif option == '5':
        exit()
    else:
        main_menu()

backup_dir, hosts_dir = check_environment()
hosts_path = '%s\hosts' % hosts_dir
main_menu()