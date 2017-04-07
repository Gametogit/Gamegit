#-*- coding: utf-8 -*-
#for test
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.config import cConfig
from resources.lib.parser import cParser
from resources.lib.player import cPlayer
import base64

SITE_IDENTIFIER = 'tous_sport_tv'
SITE_NAME = 'Tous-SportTV'
SITE_DESC = 'Streaming sports'

URL_MAIN = 'http://www.tous-sports.tv'
 
URL_SEARCH = ('http://www.beinsport-streaming.com/lecteur.php?id=', 'showLinks')
FUNCTION_SEARCH = 'showLinks'

SPORT_SPORTS = ('http://', 'load')

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
Referer = 'http://www.beinsport-streaming.com'
Referer2 = 'http://www.hdmyt.info'

sThumb = 'http://4.bp.blogspot.com/-NCJjAGZ8_wc/VlnB_BfoN3I/AAAAAAAAADM/tSynz3OCRR4/s1600-r/HA.gif'


def load(): 
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/') 
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Lancez Chaine par son Numéro (voir programme sur le site)', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://sToday')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Programme (du Jour)', 'tv.png', oOutputParameterHandler)

   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN)
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Programme (Complet)', 'tv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
 

def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard() 
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText
        showLinks(sUrl, sSearchText)
        return 
        oGui.setEndOfDirectory()
        

def __getUrl(url, pattern, referer):

    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('User-Agent',UA)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()
    sPattern = pattern
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    return aResult


def showMovies():
    oGui = cGui()
   
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    sToday = 0
    if 'sToday' in sUrl:
        sUrl = URL_MAIN
        sToday= 1
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    sPattern = '(?:<p class="Day">([^<>]+)</p>|)(?:<p class="active" style=".+?">([^<>]+)</p><span>.+?|)<span class="date">([^<>]+)</span><a href="([^"]+)" title=".+?" target="_blank">([^<>]+)(?:<span class="liens">|<i class=".+?">)'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        round = 0
        round2 = 0
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            
            
            if aEntry[0]:
               oGui.addText(SITE_IDENTIFIER,'[COLOR olive]' + aEntry[0]+ '[/COLOR]')
               if (sToday ==1):
                   round2= round2+1
            if aEntry[1]:
               oGui.addText(SITE_IDENTIFIER,'[COLOR coral]' + aEntry[1]+ '[/COLOR]')
               if 'Stream 24/24' in aEntry[1]:
                   round = 1
               else:
                   round = 0

            sTime = str(aEntry[2]).replace(' :', '')
            sTitle = str(aEntry[4]).replace(':', '')
            sUrl = str(aEntry[3])
            sThumbnail = sThumb
            
            if (round2 >1):
                break
            else:
                if (round ==0):
                    sDisplayTitle = (' (%s) %s ') % ( sTime, sTitle)
                else:
                    sDisplayTitle = (' %s ') % (sTitle)
            
            
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle) 
                oOutputParameterHandler.addParameter('sThumbnail', sThumbnail)
                oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sDisplayTitle, '', sThumbnail,'', oOutputParameterHandler)
                
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()


def showLinks(sSearch = '', channel=''):
    oGui = cGui()
    
    if sSearch:

       sUrl = sSearch
       sMovieTitle = 'Chaine ' + channel
        
    
    else:
        
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')


        sPattern = '<iframe src="(http://www.bein.+?)"'
        aResult = __getUrl(sUrl, sPattern, Referer)

        if (aResult[0] == True):
            for aEntry in aResult[1]:
                sUrl = aEntry
    
    

    sUrl = sUrl.replace('lecteur.php?id=','stream/ch') + '.php'
    sPattern = '<script type="text/javascript" src="(.+?)">'
    aResult = __getUrl(sUrl, sPattern, Referer)


    if (aResult[0] == True):
        
        sUrl = aResult[1][0]
        sUrl = sUrl.replace('http://www.hdmyt.info/channel', 'http://www.playerhd2.pw/channel')
        sPattern = '<iframe src="(http://www.playerhd2.pw.+?)"'
        aResult = __getUrl(sUrl, sPattern, Referer2)
    else:
        return   
    
    if (aResult[0] == True):
        
        sLink = 'noLink'
        round3 = 0
        while ('noLink' in sLink):
                round3 = round3 +1
                sUrl = aResult[1][0]
                sPattern = '<input type="hidden" id=".+?" value="([a-zA-Z0-9=+/]+)"\s/>'
                aResult2 = __getUrl(sUrl, sPattern, Referer2)
                
                if (round3 >10):
                    sLink = 'LinkOFF'

                if (aResult2[0] == True):
                    for aEntry in aResult2[1]:
                        content = len(aEntry)

                        if (content >20):  
                            link = base64.b64decode(aEntry)
                            link2 = base64.b64decode(link)
                            link3 = base64.b64decode(link2)
                            if '.m3u8' in link3:
                                sLink = link3
                                
                      
                            
        sUrl = sLink + '|Referer=http://www.playerhd2.pw/jwplayer6/jwplayer.flash.swf&User-Agent=Mozilla/5.0 (X11; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0 Iceweasel/42.0'
        sThumbnail = sThumb
        
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sMovieTitle)
        oGuiElement.setMediaUrl(sUrl)
        oGuiElement.setThumbnail(sThumbnail)

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return
    else:
        return
    if not sSearch:
       oGui.setEndOfDirectory()
