#encoding=utf-8

import os

# DOC_DIR = "\\\\172.19.56.18\\wordxml$\\doc"
# OUT_DIR = "\\\\172.19.56.18\\wordxml$\\out"

# DOC_DIR2 = "\\\\172.19.56.18\\wordxml$\\doc2"
# OUT_DIR2 = "\\\\172.19.56.18\\wordxml$\\out2"

# ftpinfo
FTP_SERVER = 'ftp3.dc2.fzyun.io'
FTP_USER = 'shuchang_dev'  
FTP_PWD = 'Shuchang@2018' 
FTP_OUT_DIR = "ftp://ftp3.dc2.fzyun.io/bookout"
FTP_WordDirTestBook = "/lss/test1"
FTP_XmlDirTestBook = "/bookout/lss"
FTP_WordDirChapterBook = "/FounderDeployPackage/Autotest/word/ChapterBook"
FTP_XmlDirChapterBook = "/bookout/ChapterBook"
FTP_WordDirDissertationBook = "/FounderDeployPackage/Autotest/word/DissertationBook"
FTP_XmlDirDissertationBook = "/bookout/DissertationBook"
FTP_WordDirStandardBook = "/FounderDeployPackage/Autotest/word/StandardBook"
FTP_XmlDirStandardBook = "/bookout/StandardBook"
FTP_AutoTestDir = "/FounderDeployPackage/Autotest"
PublishTaskUrl ="http://web.tsengine.dev2.fzyun.io/xmlcpTaskForward/publishTask.do"
RoutingKey = ""


# PROGRAM_FILES = "C:\\Program Files (x86)" if os.path.exists("C:\\Program Files (x86)") else "C:\\Program Files"
# SETUP_PATH = PROGRAM_FILES + u"\\Founder\\FounderWordClient"
# WORD2XML_EXE = SETUP_PATH + u"\\Fword2xml.exe"
# TEMPLATE_PATH = SETUP_PATH + u"\\Template\CMA_JATS匹配规则";
# TAG_NAME = u"NISO_JATS"
# META_PATH = SETUP_PATH + u"\\期刊元数据"
# DEFAULT_META_FILE = META_PATH + u"\\病毒学报.xml"
