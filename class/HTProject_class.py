import yaml
import os
class HTProject :
    """
    HTProject class
    """
    IsNew=False
    File=''
    #def __init__(self):

    
 #   def Crate(self,con) :   
#        Item[con]=self.
#    def __init__(self,IsNew,ProjectName, ResoureLanguage, Author,Member,Contributor,HTVersion,PVersion, BuildTime, LastChange, License, describtion, Website, HTsite, ProjectLocal,IsClock,IsFinish,NeedCheck) :
 #       if (IsNew) :
  #          self.ProjectName=ProjectName
   #         self.ResoureLanguage=ResourceLanguage
    #        
#
 #       else :
  #          open()


    class TranItem :

        def UpdateRes(self):
            """
            更新翻译文本数据,并改变tag
            """
            
        def ChangeTag(self,ntag,ac=False):
            """
            更改tag
            """    
            self.Item['Tag']=ntag
            return ac

        def __init__(self,ID):
            """
            构造函数
            """
            self.Item={
                'ID':ID,
                'Resource':'',
                'TransResource':{},
                'Tag':'',
                'Translator':[],
                'TransTime':'',
                'IsClock':False,
                'Checker':[],
                'CheckTime':''
                }        

        #def __init__() :
            
    #def __init__() :



    def ChangeCustom(self,Cf=[],Cs=[]):
        """
        修改自定义规则(后置)
        """
        if Cf!=[]:
            self.Rule['Custom']['func']==Cf
            if Cs!=[]:
                self.Rule['Custom']['string']==Cs
            else :
                return False
        
    def ChangeRule(self,chance,ac=False):
        """
        修改规则_前置函数
        """
        for i in chance.keys():
            #print(i)
            if (chance[i]!='') :
                ac=True
                #
                #
                if (i=='ReaderRule' or i=="WriterRule"):
                    self.Rule[i].append(chance[i])
                elif (i=='Custom'):
                    self.ChangeCustom(chance[i])
                else:    
                    self.Rule[i]=chance[i]    
                
                
            else:
                return False

        return ac


            
    def LoadProject(self, file):
        """
        从文件加载工程
        """
        open(file)        

    def ChangeConfig(self,chance,ac=False) :
        """
        修改工程信息
        """
        for i in chance.keys():
            #print(i)
            if (chance[i]!='') :
                self.ProjectConfig[i]=chance[i]
                ac=True

        return ac

    def AddRes(self,ID='',ac=False) :
        """
        添加新条目数据
        """
        if ID == "" :
            self.Res.append(self.TranItem(len(self.Res) + 1).__dict__)    
            print(self.Res)           
        return ac

    def Temp_Find_TransRes(self,temp,ID='',Res='',lang='en'):
        """
        临时获取翻译后数据
        """
        if ID!='':
            for i in self.Res:
                if i['Item']['ID']==ID:
                    return i['Item']['TransResource'][lang]
                else:
                    return "Not Found(ID)"
        elif Res!='':
            for i in self.Res:
                if i['Item']['Resource']==Res:
                    return i['Item']['TransResource'][lang]
                else:
                    return "Not Found(OrginRes)"
        else:
            return "Not Found(ID or OrginRes Empty)"

    def DelRes(self,ID='',Name='',ac=False):
        """
        删除条目数据
        """
        if ID != '' :
            del self.Res[ID]
        else:
            self.Res.remove(Name)

    def UpdateRes(self,NRes,ID='',ORes='',ac=False):
        """
        更新条目数据
        """
        if ID=='':
            self.Res[ID]
        else:
            for i in self.Res :
                if self.Res[i].__dict__['Resource']==ORes:
                    self.Res[i]
                else:
                    return "Error Find Resource"
        
    def __init__(self,IsNew,file=''):
        """
        构造函数
        """
        if (IsNew):
            self.IsNew=IsNew
            self.ProjectConfig={
                'ProjectName':'',
                'ResoureLanguage':'',
                'Author':[],
                'Member':[],
                'Contributor':[],
                'HTVersion':'1.0',
                'PVersion':'',
                'BuildTime':'',
                'LastChange':'',
                'License':'',
                'describtion':'',
                'Website':'',
                'HTsite':'',
                'ProjectLocal':'..',
                'IsClock':False,
                'IsFinish':False,
                'NeedCheck':True
                }
            self.Rule={
                'ReaderRuleFile':'',
                'WriterRuleFile':'',
                'CustomFile':'',
                'ReaderRule':[],
                'WriterRule':[],
                'Custom':{ 
                    'func':[] ,
                    'string':[] 
                        }
                }
            self.Res=[]  
    
        else:
            self.LoadProject(file)

h=HTProject(True)

#print(h.__dict__)
#print(h.__doc__)
#print(h.ChangeConfig({'ResoureLanguage':'Hello'}))
#print(h.ProjectConfig)
#print(h.Rule)
#print(h.Res)

h.AddRes()
h.AddRes()
h.AddRes()

#f = open(r"testProject.yaml",encoding='utf-8')
#data = f.read()
print(yaml.safe_dump(h.__dict__))
f= open("test.yaml","w+")
f.write(yaml.safe_dump(h.__dict__))
f.close()












#print(yaml.load(data))