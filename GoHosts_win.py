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
    raw_input('\n轻轻按下[Enter]退出 . . .')
    exit()

def check_environment():
    print u'正在检查系统环境',
    try:
        backup_dir = '%s\Documents\GoHosts\\backup' % os.environ['USERPROFILE']
    except:
        backup_dir = False
    try:
        hosts_dir = '%s\System32\drivers\etc' % os.environ['SYSTEMROOT']
    except:
        hosts_dir = False
    if backup_dir and hosts_dir == False:
        print u'. . . 失败'
        quit_()
    else:
        print u'. . . 成功'
        return backup_dir, hosts_dir

def back():
    raw_input('\n轻轻按下[Enter]返回主菜单 . . .')
    main_menu()

def get_time():
    timef = str(time.strftime('20%y%m%d%H%M%S'))
    return timef

def backup():
    try:
        print u'备份hosts文件',
        if not os.path.isdir(backup_dir):
            os.makedirs(backup_dir)
        backup_time = get_time()
        backup_path = '%s\hosts%s' % (backup_dir, backup_time)
        shutil.copy(hosts_path, backup_path)
        print u'. . . 成功'
        print u'备份文件路径为'
        print backup_path
    except:
        print u'. . . 失败'
        print u'请手动备份hosts文件'
        print '%s\hosts' % hosts_dir
        back()

def download():
    try:
        print u'下载hosts文件',
        req = urllib2.Request('https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts')
        hosts_dl = urllib2.urlopen(req).read()
        print '.',
        f = open('hosts', 'wb')
        print '.',
        f.write(hosts_dl)
        print '.',
        f.close
        print u'成功'
    except:
        print u'失败'
        print u'请检查网络或从以下地址手动下载'
        print 'https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts'
        back()

def install():
    try:
        print u'安装hosts文件',
        if not os.path.isfile('hosts'):
            print u'. . . 找不到文件'
            back()
        shutil.copy('hosts', hosts_dir)
        print u'. . . 成功'
        print u'安装完成，你现在可以优雅地访问网站了'
        print u'当前目录下的hosts文件可手动删除'                                         #  TODO: improve
    except:
        print u'. . . 失败'
        print u'请右键以管理员身份运行，或手动复制hosts到'
        print '%s/hosts' % hosts_dir
        back()

def auto():
    os.system('cls')
    print u'------------------- 自动向导 ---------------------'
    print
    while True:
        backup_option = raw_input('是否需要备份当前hosts？输入[y/n]选择 ')
        if backup_option == 'y'or backup_option == 'Y':
            backup()
            break
        elif backup_option == 'n' or backup_option == 'N':
            print u'hosts未备份'
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
    print u'------------------- 还原备份 --------------------'
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
            print u'（无备份文件）'
    else:
        print
        print u'（备份目录不存在）'
    print
    print '-------------------------------------------------'
    restore_option = raw_input('还原请输入hosts文件[序号]，返回请输入[n] ')
    if restore_option == 'n' or restore_option == 'N':
        backup_mgr()
    elif backup_dict:
        if restore_option in backup_dict:
            restore_path = '%s\%s' % (backup_dir, backup_dict[restore_option])
            try:
                print u'还原hosts备份',
                shutil.copy(restore_path, hosts_path)
                print u'. . . 成功'
            except:
                print u'. . . 失败'
            finally:
                back()
    else:
        restore()

def backup_mgr():
    os.system('cls')
    print u'------------------- 备份管理 --------------------'
    print
    print u'1. 备份当前hosts文件'
    print
    print u'2. 还原备份'
    print
    print u'3. 返回主菜单'
    print
    if os.path.isdir(backup_dir):
        print u'4. 打开备份目录'
        print
    print '-------------------------------------------------'
    option = raw_input('输入[序号]选择 ')
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
    print u'----------------- 下载hosts文件 -----------------'
    print
    download()
    print u'hosts文件已下载到当前目录'
    back()

def option_install():
    os.system('cls')
    print u'----------------- 安装hosts文件 -----------------'
    print
    while True:
        install_option = raw_input('确定安装当前目录下的hosts文件吗？输入[y/n]选择 ')
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
    print u'1. 自动向导（简单）'
    print
    print u'2. 备份管理'
    print
    print u'3. 下载hosts文件'
    print
    print u'4. 安装hosts文件'
    print
    print u'5. 退出'
    print
    print '=================================================='
    option = raw_input('输入[序号]选择 ')                                             #  TODO：raw_input(unicode) CMD exit
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