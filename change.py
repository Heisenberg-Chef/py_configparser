import configparser

config = configparser.ConfigParser()

config.read('init.cfs')

config.add_section('ABC')   #   添加一个ABC的section

#   config.remove_section("ABC")    #   删除ABC的section
config.set("ABC",'user','Ray')  #   添加一个ABC section的user项目，值是Ray
config.remove_option('ABC',"user")  #   删除ABC中的user项目
config.set("<SECTION>","<K>","<V>")

with open("init.cfs",'w') as f:
    config.write(f)
 
