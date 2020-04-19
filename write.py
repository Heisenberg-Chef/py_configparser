import configparser

config = configparser.ConfigParser()    #  表准的PY库实例化

config["DEFAULT"] = {'ServerAliveInterval':45,
                     'Compression':'yes',
                     'CompressionLevel':9,
                     'ForwardX11':'yes'}    #   类似于操作字典的形式

config['bitbucket.org'] = {'User':'Ray'}

with open('init.cfs','w') as configfile:
    config.write(configfile)    #   将对象写入文件。