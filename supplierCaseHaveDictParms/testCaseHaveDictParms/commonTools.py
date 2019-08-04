import configparser

#获取配置文件的参数
#根据tag,key值获取对应value
def generateParameter(tag,name):
    config = configparser.RawConfigParser()
    # config.read('params.ini',encoding="utf-8")
    config.read('./testCaseHaveDictParms/params.ini',encoding="utf-8")
    return config.get(tag, name, raw=False)

#字典-# 根据key值获取对应value
def getDictParameter(key):
    file = open('dicParms.txt','r')
    dict = eval(file.read())
    return dict[key]

#获取单个字典
def getDictionary():
    # file = open('dicParms.txt','r',encoding='UTF-8')
    file = open('./testCaseHaveDictParms/dicParms.txt','r',encoding='UTF-8')
    dictionary = eval(file.read())
    return dictionary

#获取生成字典中的参数
def getGenerateDicParams():
    # file = open('dicParms.txt','r',encoding='UTF-8')
    file2 = open('F:\cxl\script\python_script\MeiCai\supplierCaseHaveDictParms\generateDicParams.txt','r',encoding='UTF-8')
    dictionary2 = eval(file2.read())
    return dictionary2

#创建新字典
def getReadDictionary():
    no = '1122'
    dicNew = {
        'abc':'11111www.xinli.cn',
        'abc': no
    }
    file = open('text.txt','w+')
    file.write(str(dicNew))
    file.close()

#获取供应商单号


def getParms():
    dictParms = getGenerateDicParams()
    print('111',dictParms['no'])

    # print(getGenerateDicParams())







if __name__ =='__main__':
    getParms()
    # getReadDictionary()
    # generateParameterS()
    # getDictionarys()
    # getParms()
    # dragScrollBar()
    # getParms()