import configparser
import sys
config = configparser.ConfigParser()

#   查找内容，类似于字典

config.read('init.cfs')

print(config.sections())    #   ['bitbucket.org']

print('bytebong.com' in config) # False
print('bitbucket.org' in config) # True

#print(config['bitbucket.org'].get('user'))     that okay
print(config['bitbucket.org']['user'])  #   also alright

#   print(config['bitbucket.org']['abc'])   #   KeyError: 'abc'#
print(config['bitbucket.org'])          #<Section: bitbucket.org>

print(config.items('bitbucket.org'))    #   找到'bitbucket.org'下面的所有键值对，他是包含DEFAULT的数值的[('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes'), ('user', 'Ray')]

print(config.get('bitbucket.org','serveraliveinterval'))   # 找到'bitbucket.org'下面的user的value,

print('*'*50)
for key in config['DEFAULT']:   #  迭代打印
    print(key)
    
try:    
    print(config.options('DEFAULT'))    #   不能打印DEFAULT功能与上面for循环类似    configparser.NoSectionError: No section: 'DEFAULT'
except Exception as e:
    print(e)
finally:
    sys.exit()