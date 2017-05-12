# -*- coding:gbk -*-

import urllib2
import os
import time
import shutil


version = '0.1'

def out():
    out = raw_input('\n轻轻按下[Enter]退出 . . .')
    exit()


print 'Go Hosts for Windows v%s' % version
print '-'*40
#  title

while 1:
    backup_option = raw_input('是否需要备份当前hosts？输入[y/n]选择 ')
    if backup_option == 'y'or backup_option == 'Y':
        try:
            print '备份hosts文件',
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
            print '成功'
            print '\n备份文件路径为\n"%s"' % backup_path
            break
        except:
            print '失败'
            print '-' * 40
            print '请手动备份hosts文件'
            print '"C:\Windows\System32\drivers\etc\hosts"'
            out()
    elif backup_option == 'n'or backup_option == 'N':
        break
    else:
        continue
print '-'*40
#  backup

try:
    print '下载hosts文件',
    req = urllib2.Request('https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts')
    hosts_dl = urllib2.urlopen(req).read()
    print '.',
    f = open('hosts','wb')
    print '.',
    f.write(hosts_dl)
    print '.',
    f.close
    print '成功'
except:
    print '失败'
    print '-'*40
    print '请检查网络或从以下地址手动下载'
    print 'https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts'
    out()
#  download hosts file

try:
    print '检查系统目录',
    windir = os.environ['SYSTEMROOT']
    target_path = '%s\System32\drivers\etc\hosts' % windir
    print '. . . 成功'
except:
    print '. . . 失败'
    print '-'*40
    print '请手动复制hosts文件到"C:\Windows\System32\drivers\etc\\"'
    out()
# get the target path

try:
    print '移动hosts文件',
    shutil.copy('hosts', target_path)
    print '. . . 成功'
    print '-'*40
    print '安装完成，你现在可以优雅地访问网站了'
    print '当前目录下的hosts文件可手动删除'              # TODO: improve
except:
    print '. . . 失败'
    print '-'*40
    print '请右键以管理员身份运行，或手动复制hosts到\n"%s\System32\drivers\etc\\"' % windir
finally:
    out()
#  move hosts file