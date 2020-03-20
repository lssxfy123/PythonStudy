#coding:utf-8
import os,os.path,re,sys,time,uuid
import xml.etree.ElementTree as ET
from xml.dom import minidom
import urllib
import socket
import ftplib
import config

#--------------connect ftp----------
def ftp_connect():
    ''' 连接ftp '''
    ftp = ftplib.FTP()  
    # ftp.set_debuglevel(2)
    ftp.set_pasv(True)

    try:
        ftp.connect(config.FTP_SERVER,21)
        print(ftp.welcome)
    except (socket.error, socket.gaierror) as e:
        print ("Error: connect ftpserver '%s' failed! %s") % (config.FTP_SERVER, e)
        exit()

    try:
        ftp.login(config.FTP_USER,config.FTP_PWD)  
        print("ftp://{0} login successfully!".format(config.FTP_SERVER))
    except(ftplib.error_perm) as e:
        print("Error: login failed, error code: {0}".format(e))
        exit()

    return ftp

#-------------file operate---------

def deleteFiles(target_dir):
    if os.path.exists(target_dir):
        for dirOrFile in os.listdir(target_dir):
            target_dirOrFile=os.sep.join([target_dir,dirOrFile])
            if os.path.isdir(target_dirOrFile):
                deleteFiles(target_dirOrFile+os.sep)
                os.rmdir(target_dirOrFile)
            else:
                os.remove(target_dirOrFile)

def deleteFile(target_File):
    if os.path.exists(target_File):
        os.remove(target_File)
        return True
    return False

def makedir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    isExist=os.path.exists(path)
    if not isExist:
        os.mkdir(path)
        #print(path+" 创建成功!")
        return True
    else:
        #print(path+" 已存在!")
        return False

#----------------read/write xml---------
def read_xml(in_path):  
    '''''读取并解析xml文件 
       in_path: xml路径 
       return: ElementTree'''  
    tree = ET.ElementTree()
    tree.parse(in_path)  
    return tree

def write_xml(tree, out_path):  
    '''''将xml文件写出 
       tree: xml树 
       out_path: 写出路径'''  
    tree.write(out_path, encoding="utf-8",xml_declaration=False)

#---------------search -----    
def find_nodes(tree, path):  
    '''''查找某个路径匹配的所有节点 
       tree: xml树 
       path: 节点路径'''  
    return tree.findall(path)

def get_node_by_keyvalue(nodelist, kv_map):  
    '''''根据属性及属性值定位符合的节点，返回节点 
       nodelist: 节点列表 
       kv_map: 匹配属性及属性值map'''  
    result_nodes = []  
    for node in nodelist:  
        if if_match(node, kv_map):  
            result_nodes.append(node)  
    return result_nodes

def if_match(node, kv_map):  
    '''''判断某个节点是否包含所有传入参数属性 
       node: 节点 
       kv_map: 属性及属性值组成的map'''  
    for key in kv_map:  
        if node.get(key) != kv_map.get(key):  
            return False  
    return True

#---------------change -----    
def change_node_properties(nodelist, kv_map, is_delete=False):  
    '''''修改/增加 /删除 节点的属性及属性值 
       nodelist: 节点列表 
       kv_map:属性及属性值map'''  
    for node in nodelist:  
        for key in kv_map:  
            if is_delete:   
                if key in node.attrib:  
                    del node.attrib[key]  
            else:  
                node.set(key, kv_map.get(key))

def change_node_text(nodelist, text, is_add=False, is_delete=False):  
    '''''改变/增加/删除一个节点的文本 
       nodelist:节点列表 
       text : 更新后的文本'''  
    for node in nodelist:  
        if is_add:  
            node.text += text  
        elif is_delete:  
            node.text = ""  
        else:  
            node.text = text

def getXmlString(element,defaultEncoding='utf-8'):
    '''''
          根据节点返回格式化的xml字符串
    '''
    try:
      rough_string = ET.tostring(element, defaultEncoding)
      reparsed = minidom.parseString(rough_string)
      return reparsed.toprettyxml(indent=" " , encoding=defaultEncoding)
    except:
      print('getXmlString:传入的节点不能正确转换为xml，请检查传入的节点是否正确')
      return ''

#str转unicode
def to_unicode(s, encoding):
    return  s
    # if isinstance(s, str):
    #   return s
    # else:
    #   return  unicode(s, encoding)

def executestructure(worddir,xmldir,booktype):
    #获取word文件夹路径      
    inputWordPath=config.FTP_AutoTestDir  
    var_fullInputWordPath=worddir + r"/" 
    
    #获取存放xml文件的文件夹路径    
    outputXmlPath=config.FTP_AutoTestDir 
    var_fullOutputXmlPath=xmldir + r"/" 
    
    #获取FTP的IP地址  
    var_ftpName=config.FTP_SERVER
    
    #获取FTP的端口   
    var_ftpPort="21"
    
    #获取FTP的用户名  
    var_ftpUserName=config.FTP_USER
    
    #获取FTP的密码   
    var_ftpUserPassword=config.FTP_PWD  

    #存放command的文件夹
    var_root_path=os.getcwd()   
    var_commandPath=var_root_path+"\\Command"
    makedir(var_commandPath)
    var_commandPath_bookType=var_commandPath+"\\"+booktype
    makedir(var_commandPath_bookType)
    
    #读取xml文件
    var_xmlTemplateFilePath=var_root_path+"\\cmdsample-ftp.xml"   
    tree = read_xml(var_xmlTemplateFilePath)   
    
    #修改节点的FTP信息 
    var_ftpParams=find_nodes(tree, "Params/Param/Param")   
    var_ftpNameParamNodes=get_node_by_keyvalue(var_ftpParams, {"name":"ftpName"})
    change_node_properties(var_ftpNameParamNodes, {"value": var_ftpName})
    var_ftpPortParamNodes=get_node_by_keyvalue(var_ftpParams, {"name":"ftpPort"})
    change_node_properties(var_ftpPortParamNodes, {"value": var_ftpPort})
    var_ftpUserNameParamNodes=get_node_by_keyvalue(var_ftpParams, {"name":"ftpUserName"})
    change_node_properties(var_ftpUserNameParamNodes, {"value": var_ftpUserName})
    var_ftpUserPasswordParamNodes=get_node_by_keyvalue(var_ftpParams, {"name":"ftpUserPassword"})
    change_node_properties(var_ftpUserPasswordParamNodes, {"value": var_ftpUserPassword})

    var_root=tree.getroot()    
    var_params=find_nodes(tree, "Params/Param")   
    var_metaParamNodes=get_node_by_keyvalue(var_params, {"name":"journalMeta"})
    var_contentParamNodes=get_node_by_keyvalue(var_params, {"name":"content"})
    var_resultParamNodes=get_node_by_keyvalue(var_params, {"name":"result"})
    var_bookTypeParamNodes=get_node_by_keyvalue(var_params, {"name":"bookType"})
    
    #修改journalMeta节点value值
    metaFilePath=re.sub(r'\\(\d+).(\d+).(\d+).(\d+)','',inputWordPath)+os.sep+"meta.xml"    
    change_node_properties(var_metaParamNodes, {"value": metaFilePath.replace("\\",r'/').replace(r"//",r'/').replace(r"/share","")})

    #修改bookType节点的value值
    change_node_properties(var_bookTypeParamNodes, {"value": booktype})  

    #获取ftp上指定目录中的文件信息    
    ftpWordDir = "%s/" % worddir
    global var_ftp
    var_ftp.cwd(ftpWordDir)  
    filelist=var_ftp.nlst()      
    var_wordCount=0    

    for dirOrFile in filelist:           
        target_dirOrFile=os.sep.join([var_fullInputWordPath,dirOrFile])          
        
        if os.path.isdir(target_dirOrFile):               
            continue            
        else:                
            file_extension= os.path.splitext(dirOrFile)
            if file_extension[1].endswith('docx') or file_extension[1].endswith('doc'):                                  
                wordFileFullName=to_unicode(dirOrFile,"utf-8")
                print(var_fullInputWordPath+wordFileFullName)
                xmlFileFullName=to_unicode(file_extension[0],"utf-8")+".xml"                   

                #修改CommandId节点
                cmdIdNode=var_root.find("CmdId")               
                cmdIdNode.text=str(uuid.uuid1())

                #修改TaskOverTime节点
                taskOverTime=var_root.find("TaskOverTime")
                taskOverTime.text="300"

                #修改operate节点
                tempFullOutputXmlPath=var_fullOutputXmlPath
                operateNode=var_root.find("operate")
                operateNodeTextSplitList=operateNode.text.split(',')                                    
                strList=operateNodeTextSplitList[1].split(':')                
                xmlPath=re.sub(r'\\',r'/',tempFullOutputXmlPath)+xmlFileFullName
                xmlPath=re.sub(r'//(\d+).(\d+).(\d+).(\d+)','',xmlPath).replace(r"/share","")                   
                operateNodeTextSplitList[1]=to_unicode(strList[0],"gbk")+":\""+to_unicode(xmlPath,"gbk")+"\""                                                   
                operateNode.text=",".join(operateNodeTextSplitList)        
             
                #修改name为content节点                    
                text=re.sub(r'\\(\d+).(\d+).(\d+).(\d+)','',var_fullInputWordPath).replace("\\",'/').replace(r"//",r'/').replace(r"/share","")+wordFileFullName                      
                change_node_properties(var_contentParamNodes, {"value": to_unicode(text,"gbk")})               

                #修改name为result节点
                text=re.sub(r'\\(\d+).(\d+).(\d+).(\d+)','',tempFullOutputXmlPath).replace("\\",'/').replace(r"//",r'/').replace(r"/share","")+xmlFileFullName                      
                change_node_properties(var_resultParamNodes, {"value": to_unicode(text,"gbk")})                    
                var_commandXmlPath = var_commandPath_bookType+"\\%scommand.xml"%file_extension[0]                    
                                                
                write_xml(tree, var_commandXmlPath)
                with open(var_commandXmlPath) as file:
                    var_command = file.read()                        
                    
                #url='http://172.19.57.213:8080/xmlcpTaskForward/publishTask.do'
                #url='http://ts-web.engine-ts.test.fzyun.io/xmlcpTaskForward/publishTask.do'
                url=config.PublishTaskUrl
                routingKey=config.RoutingKey
                callBackUrl='http://www.baidu.com'
                queueName='word-auto-test'
                if routingKey.strip()=='':                        
                    data={"cmd":var_command,"queueName":queueName,"callBackUrl":callBackUrl}
                else:
                    data={"cmd":var_command,"queueName":queueName,"callBackUrl":callBackUrl,"routingKey":routingKey}
                data=urllib.parse.urlencode(data).encode('utf-8')
                req=urllib.request.Request(url,data=data)
                try:
                    response=urllib.request.urlopen(req,timeout=120)
                except urllib.error.HTTPError as err:
                    print(err.code)
                    break
                except (urllib.error.URLError) as err:
                    print(err)
                    break
                else:
                    code=response.getcode()                    
                    print('HTTP code:',code)
                    page=response.read().decode('utf-8')                    
                    print(page)
                    response.close()
                    var_wordCount=var_wordCount+1
                    time.sleep(2)

    global var_wordTotalCount              
    var_wordTotalCount=var_wordTotalCount+var_wordCount    
    print("Word to XML Successfully! WordCount=%s" % var_wordCount)        
            

if __name__=="__main__":
    #结构化成功的word总数
    var_wordTotalCount=0
    #连接ftp
    var_ftp=ftp_connect()
    
    #executestructure(config.FTP_WordDirTestBook,config.FTP_XmlDirTestBook,"TestBook")
    executestructure(config.FTP_WordDirChapterBook,config.FTP_XmlDirChapterBook,"ChapterBook")
    # executestructure(config.FTP_WordDirDissertationBook,config.FTP_XmlDirDissertationBook,"DissertationBook")
    # executestructure(config.FTP_WordDirStandardBook,config.FTP_XmlDirStandardBook,"StandardBook")
    
    print("Word to XML Successfully! WordTotalCount=%s" % var_wordTotalCount)  
    
   
   





