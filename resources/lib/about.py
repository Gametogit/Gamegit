#-*- coding: utf-8 -*-
#Venom
from config import cConfig
from resources.lib.gui.gui import cGui 
import urllib, urllib2
import xbmc, xbmcgui, xbmcaddon
import xbmcvfs
import sys, datetime, time, os
sLibrary = xbmc.translatePath(cConfig().getAddonPath())
sys.path.append (sLibrary) 

from resources.lib.handler.requestHandler import cRequestHandler

class cAbout:

    
    def GGcreateDialogOK(self, label):
        oDialog = xbmcgui.Dialog()
        oDialog.ok('vStream', label)  
        return oDialog

    def GGcreateDialogYesNo(self, label):
        oDialog = xbmcgui.Dialog()
        qst = oDialog.yesno("vStream", label)
        return qst

    def GGcreateDialog(self, sSite):
        
        oDialog = xbmcgui.DialogProgress()
        oDialog.create(sSite)
        return oDialog

    def GGupdateDialog2(self, dialog, label = ''):
        dialog.update(0, 'Chargement: '+str(label))

    def GGfinishDialog(self, dialog):
        if xbmcgui.Window(10101).getProperty('search') != 'true':
           dialog.close()
           del dialog
           return False

    def GGupdateDialog3(self, dialog, mode, total, repo, test, maj):
        if 'Maj Fichier' in maj:
            cConfig.COUNT = cConfig.COUNT -1
        iPercent = int(float(cConfig.COUNT * 100) / total)
        dialog.update(iPercent,'\n\n\n\n')
        compteur = '[COLOR skyblue]' +str(cConfig.COUNT)+'/'+str(total)+'[/COLOR]'   
        if 'Github' in repo:
            dialog.update(iPercent, str(mode)+str(compteur)+str(repo)+'\n\n'+str(test)+'\n'+str(maj))
        else:
            dialog.update(iPercent, str(mode)+str(compteur)+str(repo)+'\n'+str(test)+'\n'+str(maj))
        cConfig.COUNT += 1

    def GGupdate(self):
        xbmc.executebuiltin("Container.Refresh")


    def siteOff(self):
        
        folder = 'plugin.video.vstream/resources/sites/'
        sMath = cConfig().getAddonPath().replace('plugin.video.vstream', '') 
        sFolder = os.path.join(sMath, folder)
        sFolder = sFolder.replace('\\', '/')
        aNameList = []
        items = os.listdir(unicode(sFolder, 'utf-8'))
        items.sort()
        for sItemName in items:
            sFilePath = os.path.join(unicode(sFolder, 'utf-8'), sItemName)
            #xbox hack
            sFilePath = sFilePath.replace('\\', '/')
            
            noErase =  ['tous_sport_tv.py', 'livetv_sport.py']
            if (os.path.isdir(sFilePath) == False):
                if (sFilePath.lower().endswith('py')):
                    if not sItemName in noErase:
                       aNameList.append(sItemName)
        return aNameList  
            
    
    def size(self, filepath):
        
        if os.path.exists(filepath):
             
           file=open(filepath)
           Content = file.read()
           file.close()
           
           return len(Content)
        
        else:
           
           if ('xxxxx') in filepath:   
              
               return len(Content)
           else:
              
               Content = "1"
               return len(Content)
    

    def getUpdate(self):
        
        service_time = cConfig().getSetting('service_time')
        if (service_time):
                        
            time_sleep = datetime.timedelta(hours=6)
            time_now = datetime.datetime.now()
            time_service = self.__strptime(service_time, "%Y-%m-%d %H:%M:%S.%f")
            
            
            if (time_now - time_service > time_sleep):
                
                self.checkupdate()
            else:
                cConfig().setSetting('service_last', str(time_sleep + time_service))  

        return
      
    
    def __strptime(self, date, format):
        try:
            date = datetime.datetime.strptime(date, format)
        except TypeError:
            date = datetime.datetime(*(time.strptime(date, format)[0:6]))
        return date
        

    def getRootPath(self, folder):
        
        sMath = cConfig().getAddonPath().replace('plugin.video.vstream', '') 
        sFolder = os.path.join(sMath, folder)
        # xbox hack        
        sFolder = sFolder.replace('\\', '/')
        
        sFolder = sFolder.replace('resources/lib/home.py', 'plugin.video.vstream/resources/lib/home.py')
        sFolder = sFolder.replace('resources/lib/about.py', 'plugin.video.vstream/resources/lib/about.py')
        sFolder = sFolder.replace('resources/lib/statistic.py', 'plugin.video.vstream/resources/lib/statistic.py')
        sFolder = sFolder.replace('resources/lib/tous_sport_tv.py', 'plugin.video.vstream/resources/sites/tous_sport_tv.py')
       
        return sFolder

    
    def resultGit(self):
        
        try:    import json
        except: import simplejson as json
        try:
            
            sUrl = 'https://api.github.com/repos/Kodi-vStream/venom-xbmc-addons/contents/plugin.video.vstream/resources/sites'
            
            
            oRequestHandler = cRequestHandler(sUrl)
            sHtmlContent = oRequestHandler.request();
            result = json.loads(sHtmlContent)
            
            sUrl = 'https://api.github.com/repos/Kodi-vStream/venom-xbmc-addons/contents/plugin.video.vstream/resources/hosters'
                        
            oRequestHandler = cRequestHandler(sUrl)
            sHtmlContent = oRequestHandler.request();
            result += json.loads(sHtmlContent)
                     
            
        except:
            cConfig().showInfo("Maj Vstream", "Erreur: Veuillez réessayer plus tard", 3)
            return False
        return result

    
    def resultGit2(self, link):
        
        try:    import json
        except: import simplejson as json
        
        try:
            dialog = self.GGcreateDialog('Mise à jour en cours')
            
            if (link == 'link1'):
               sUrl = ['vstream/resources/sites','vstream/resources/hosters','vstream/resources','vstream', 'vstream/resources/lib/handler', 'vstream/resources/lib/gui', 'vstream/resources/lib', 'vstream/resources/language/French', 'vstream/resources/skins/default/720p', 'Gamegit/contents/resources/lib']
               
              
            if (link == 'link2'):
               sUrl = ['vstream/resources/art/sites', 'vstream/resources/art/tv', 'vstream/resources/art', 'vstream/resources/language/English', 'vstream/resources/skins/default/media']

            total = len(sUrl)
            total2 = 0
            cConfig.COUNT = 1

            mode = "Chargement:  "
            repo = '    [ via Repo Github vStream Beta ]'
            maj = ''
            for url in sUrl:
                url2 = 'https://api.github.com/repos/Kodi-vStream/venom-xbmc-addons/contents/plugin.video.' + url
                if 'Gamegit' in url:
                    url2 = 'https://api.github.com/repos/Gametogit/' + url
                
                    
                test = '[COLOR skyblue]'+'>> '+url+ '[/COLOR]'

                self.GGupdateDialog3(dialog, mode, total, repo, test, maj)
                
                oRequestHandler = cRequestHandler(url2)
                sHtmlContent = oRequestHandler.request();
                

                if ('vstream/resources/lib' == url):
                    sHtmlContent = sHtmlContent.replace('about.py', 'xxxxx').replace('home.py','xxxxx').replace('statistic.py', 'xxxxx')
                if 'Gamegit' in url:
                    sHtmlContent = sHtmlContent.replace('default.py', 'xxxxx')
                if ('vstream/resources/sites' == url):
                    sHtmlContent = sHtmlContent.replace('en_cours', 'xxxxx').replace('trash', 'xxxxx')

                if (total2 ==0):
                    result = json.loads(sHtmlContent)
                else:
                    result += json.loads(sHtmlContent)
                total2 = total2+1
            
            endList = "[COLOR skyblue] [ OK ][/COLOR]\n\n[COLOR skyblue] >> Liste Fichiers Téléchargées - Patientez...[/COLOR]"
            
            erase = "\n\n\n\n"
            self.GGupdateDialog2(dialog, erase)
            self.GGupdateDialog2(dialog, endList)
            xbmc.sleep(2000)
            self.GGupdateDialog2(dialog, erase)

        except:
              cConfig().showInfo("Maj Vstream", "Erreur: Veuillez réessayer plus tard", 3)
              return False
        return result

    
    def checkupdate(self):
            
            service_time = cConfig().getSetting('service_time')            
            
            result = self.resultGit()
            sDownl = 0
            
            if result:
            
                for i in result:
                    
                    try: 
                        rootpath = self.getRootPath(i['path'])
                        
                        if (self.size(rootpath) != i['size']):
                            
                            sDownl = sDownl+1
                            break
                    except:
                        pass
                if (sDownl != 0):
                     
                    cConfig().setSetting('service_time', str(datetime.datetime.now()))
                    cConfig().showInfo("vStream", "Mise à jour disponible")
     
                      
                else:
                    
                    cConfig().setSetting('service_time', str(datetime.datetime.now()))
            return
    
    
    def checkdownload(self, link):
            
            if (link == 'link1'):
                siteLocal = self.siteOff()
                siteKO = []
                siteKO2 = []
                siteGit = []
            
            result = self.resultGit2(link)
            total = len(result)
            
            dialog = self.GGcreateDialog('Mise à jour')
            
            site = []
            sdown = 0
            cConfig.COUNT = 1
            
            mode = "Vérification:  "
            vstream = "[COLOR skyblue]>> vStream déjà à jour  ;-)[/COLOR]"
            repo = ''
            
            if result: 
                
                for i in result:
                    
                    maj = ''
                    c = i['name']
                    
                    if (link == 'link1') and ('plugin.video.vstream/resources/sites/' in i['path']):
                        siteGit.append(c)
                    
                    test = '[COLOR skyblue]' +'>> ' + c + '[/COLOR]'
                    self.GGupdateDialog3(dialog, mode, total, repo, test, maj)
                    
                    try:
                        rootpath = self.getRootPath(i['path'])
                        
                        if (self.size(rootpath) != i['size']):
                            try:
                                
                                maj = '[COLOR lime]' + 'Maj Fichier:  ' + c
                                self.GGupdateDialog3(dialog, mode, total, repo, test, maj)
                                self.__download(i['download_url'], rootpath)
                                site.append("[COLOR lime]"+i['name'].encode("utf-8")+"[/COLOR]")
                                sdown = sdown+1
                            except:
                                site.append("[COLOR red]"+i['name'].encode("utf-8")+"[/COLOR]")
                                sdown = sdown+1
                                pass
                    except:
                        pass
                
                if (link == 'link1'):
                    for a in siteLocal:
                        if a in siteGit:
                           pass
                        else:
                             b = a.replace('.py','')
                             siteKO.append(a.encode("utf-8"))
                             siteKO2.append("[COLOR skyblue]"+b.encode("utf-8")+"[/COLOR]")
                       
                
                self.GGfinishDialog(dialog)
                compteur = '[COLOR skyblue]' +str(sdown)+'/'+str(total)+'[/COLOR]'

                if sdown > 0:
                   sContent = "Fichier mis à jour:   %s \n %s" %  (compteur, site)
                else:
                    sContent = "Fichier mis à jour:   %s \n\n     %s" %  (compteur, vstream)                
                fin = self.GGcreateDialogOK(sContent)

                if (link == 'link1'):
                    t = len(siteKO)
                    
                    if (t >0) and (t <15) and (siteGit >40):
                            sContent = "Les sites suivants ne fonctionnent plus. \nVoulez-vous les désactiver de vStream ? \n %s" %  (siteKO2)
                            oDialog = self.GGcreateDialogYesNo(sContent)
                            if (oDialog == 1):
                                for a in siteKO:
                                    self.__erase(a)
                                    cConfig().showInfo('vStream' ,'Sites désactivés', 3)

                for s in site:
                    if ('about.py' in s):
                        sContent = '[COLOR skyblue]' + 'Attention !!' + '[/COLOR]' + '\nLe fichier  ' + '[COLOR lime]' + 'about.py ' + '[/COLOR]' + ' a été MAJ.' + '\nVeuillez relancer le lien' + '[COLOR green]' + '  Maj (Sites/Hosters/Configs)' + '[/COLOR]' + '\npour être 100% à jour et éviter les bugs.'
                        fin2 = self.GGcreateDialogOK(sContent)
                
                self.GGupdate()
            return
            
    def __download(self, WebUrl, RootUrl):
        try:
            inf = urllib.urlopen(WebUrl)
            f = xbmcvfs.File(RootUrl, 'w')
            #save it
            line = inf.read()         
            f.write(line)
            
            inf.close()
            f.close()
        except:
            pass
        return

    def __erase(self, siteName):
        try:
            
            folder = 'plugin.video.vstream/resources/sites/'
            sMath = cConfig().getAddonPath().replace('plugin.video.vstream', '') 
            sFolder = os.path.join(sMath, folder)
            oldName = sFolder + siteName
            newName =  sFolder + siteName + '.desactiver'
            
            xbmcvfs.rename(oldName, newName)
            
        except:
            pass
        return
        
    def TextBoxes(self, heading, anounce):
        class TextBox():
            # constants
            WINDOW = 10147
            CONTROL_LABEL = 1
            CONTROL_TEXTBOX = 5

            def __init__( self, *args, **kwargs):
                # activate the text viewer window
                xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )
                # get window
                self.win = xbmcgui.Window( self.WINDOW )
                # give window time to initialize
                xbmc.sleep( 500 )
                self.setControls()

            def setControls( self ):
                # set heading
                self.win.getControl( self.CONTROL_LABEL ).setLabel(heading)
                try:
                    f = open(anounce)
                    text = f.read()
                except: text=anounce
                self.win.getControl( self.CONTROL_TEXTBOX ).setText(text)
                return
        TextBox()
