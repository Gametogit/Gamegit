#-*- coding: utf-8 -*-
#Venom.
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.siteHandler import cSiteHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.db import cDb
import os
import urllib
import xbmc, xbmcgui

SITE_IDENTIFIER = 'cHome'
SITE_NAME = 'Home'

#temp d'execution
#import time
#tmps1=time.time()
# tmps2=time.time()-tmps1
# print "Temps d'execution = %f" %tmps2

class cHome:


    def load(self):
        oGui = cGui()
        oConfig = cConfig()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showSearch', oConfig.getlanguage(30076), 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('themoviedb_org', 'load', oConfig.getlanguage(30088), 'searchtmdb.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        # oGui.addDir('freebox', 'load', oConfig.getlanguage(30115), 'tv.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('freebox', 'load', oConfig.getlanguage(30115), 'tv.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showReplay', oConfig.getlanguage(30117), 'replay.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', oConfig.getlanguage(30120), 'films.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showSeries', oConfig.getlanguage(30121), 'series.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showAnimes', oConfig.getlanguage(30122), 'animes.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showDocs', oConfig.getlanguage(30112), 'doc.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SPORT_SPORTS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30113), 'sport.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showNets', oConfig.getlanguage(30114), 'buzz.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('cTrakt', 'getLoad', 'Trakt (bêta)', 'trakt.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('cDownload', 'getDownload', oConfig.getlanguage(30202), 'download.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('cLibrary', 'getLibrary', oConfig.getlanguage(30300), 'library.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('globalSources', 'showSources', oConfig.getlanguage(30116), 'host.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir('cFav', 'getFavourites', oConfig.getlanguage(30210), 'mark.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        # oGui.addDir('globalParametre', 'showSources', '[COLOR teal]'+oConfig.getlanguage(30023)+'[/COLOR]', 'param.png', oOutputParameterHandler)


        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showUpdate', '[COLOR green]Mettre à jour vStream (Sites/Hosters/Configs)[/COLOR]', 'update.png', oOutputParameterHandler)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oGui.addDir(SITE_IDENTIFIER, 'showUpdate2', '[COLOR green]Mettre à jour vStream (Art/Skin/Language)[/COLOR]', 'update.png', oOutputParameterHandler)
        
        oGui.setEndOfDirectory()
        if (cConfig().getSetting("active-view") == 'true'):
            xbmc.executebuiltin('Container.SetViewMode(%s)' % cConfig().getSetting('accueil-view'))

    def showUpdate(self):
        try:
            from resources.lib.about import cAbout
            link = 'link1'
            cAbout().checkdownload(link)
        except:
            pass
        return

    def showUpdate2(self):
        try:
            from resources.lib.about import cAbout
            link = 'link2'
            cAbout().checkdownload(link)
        except:
            pass
        return

    def showDocs(self):
        oGui = cGui()
        oConfig = cConfig()

        # Affiche les Nouveautés Documentaires
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'DOC_NEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30112), oConfig.getlanguage(30101)), 'news.png', oOutputParameterHandler)

        # Affiche les Genres Documentaires
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'DOC_GENRES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30112), oConfig.getlanguage(30105)), 'genres.png', oOutputParameterHandler)

        # Affiche les Sources Documentaires
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'DOC_DOCS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30138), 'host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showNets(self):
        oGui = cGui()
        oConfig = cConfig()

        # Affiche les Nouveautés Vidéos
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'NETS_NEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30114), oConfig.getlanguage(30101)), 'news.png', oOutputParameterHandler)

        # Affiche les Genres Vidéos
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'NETS_GENRES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30114), oConfig.getlanguage(30105)), 'genres.png', oOutputParameterHandler)

        # Affiche les Sources Vidéos
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_NETS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30138), 'host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showMovies(self):
        oGui = cGui()
        oConfig = cConfig()

        oOutputParameterHandler = cOutputParameterHandler()
        #self.__callpluging('MOVIE_NEWS', 'films_news.png')
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_NEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30101)), 'films_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_HD')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30160)), 'films_hd.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_VIEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30102)), 'films_views.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_COMMENTS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30103)), 'films_comments.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_NOTES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30104)), 'films_notes.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_GENRES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30105)), 'films_genres.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_ANNEES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30120), oConfig.getlanguage(30106)), 'films_annees.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_VF')
        # oGui.addDir(SITE_IDENTIFIER, 'callpluging', '[COLOR '+color_films+']'+oConfig.getlanguage(30134)+'[/COLOR]', 'films_vf.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_VOSTFR')
        # oGui.addDir(SITE_IDENTIFIER, 'callpluging', '[COLOR '+color_films+']'+oConfig.getlanguage(30135)+'[/COLOR]', 'films_vostfr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'MOVIE_MOVIE')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30138), 'films_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showSeries(self):
        oGui = cGui()
        oConfig = cConfig()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_NEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30121), oConfig.getlanguage(30101)), 'series_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_HD')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30121), oConfig.getlanguage(30160)), 'films_hd.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_GENRES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30121), oConfig.getlanguage(30105)), 'series_genres.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_ANNEES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30121), oConfig.getlanguage(30106)), 'series_annees.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_VFS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30121), oConfig.getlanguage(30107)), 'series_vf.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_VOSTFRS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30121), oConfig.getlanguage(30108)), 'series_vostfr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'SERIE_SERIES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30138), 'series_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showAnimes(self):
        oGui = cGui()
        oConfig = cConfig()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_NEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30122), oConfig.getlanguage(30101)), 'animes_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_VFS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30122), oConfig.getlanguage(30107)), 'animes_vf.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_VOSTFRS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30122), oConfig.getlanguage(30108)), 'animes_vostfr.png', oOutputParameterHandler)

        #non utiliser ANIM_MOVIES

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_GENRES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30122), oConfig.getlanguage(30105)), 'animes_genres.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_ANNEES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30122), oConfig.getlanguage(30106)), 'animes_annees.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_ENFANTS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30122), oConfig.getlanguage(30109)), 'animes_enfants.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'ANIM_ANIMS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30138), 'animes_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showReplay(self):
        oGui = cGui()
        oConfig = cConfig()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'REPLAYTV_NEWS')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30117), oConfig.getlanguage(30101)), 'replay_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'REPLAYTV_GENRES')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', '%s (%s)' % (oConfig.getlanguage(30117), oConfig.getlanguage(30105)), 'replay_genres.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'REPLAYTV_REPLAYTV')
        oGui.addDir(SITE_IDENTIFIER, 'callpluging', oConfig.getlanguage(30138), 'replay_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showSources(self):
        oGui = cGui()

        oPluginHandler = cPluginHandler()
        aPlugins = oPluginHandler.getAvailablePlugins()
        for aPlugin in aPlugins:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
            icon = 'sites/%s.png' % (aPlugin[1])
            oGui.addDir(aPlugin[1], 'load', aPlugin[0], icon, oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showSearchText(self):
        oGui = cGui()
        oConfig = cConfig()

        oInputParameterHandler = cInputParameterHandler()
        sDisp = oInputParameterHandler.getValue('disp')
        sType = oInputParameterHandler.getValue('type')

        sSearchText = oGui.showKeyBoard()
        if not sSearchText:
            return False
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('searchtext', sSearchText)
        oOutputParameterHandler.addParameter('disp', sDisp)
        oOutputParameterHandler.addParameter('type', sType)
        oOutputParameterHandler.addParameter('readdb', 'True')
        oGui.addDir('globalSearch', 'none', '%s: %s' % (oConfig.getlanguage(30076), sSearchText), 'search.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()

    def showSearch(self):

        xbmcgui.Window(10101).clearProperty('search_text')

        oGui = cGui()
        oConfig = cConfig()

        #affiche le texte de recherche si exist
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = False
        sSite = False


        if oInputParameterHandler.exist('searchtext'):
            sSearchText = oInputParameterHandler.getValue('searchtext')
            oGui.addText('globalSearch', '[COLOR khaki]%s: %s[/COLOR]' % (oConfig.getlanguage(30076), sSearchText), 'none.png')
            sSite = 'globalSearch'
        else:
            sSite = 'cHome'

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('searchtext', sSearchText)
        oOutputParameterHandler.addParameter('disp', 'search1')
        oOutputParameterHandler.addParameter('type', oConfig.getSetting('search1_type'))
        oOutputParameterHandler.addParameter('readdb', 'True')
        sLabel1 = oConfig.getlanguage(30077)+": "+oConfig.getSetting('search1_label')
        oGui.addDir(sSite, 'showSearchText', sLabel1, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('searchtext', sSearchText)
        oOutputParameterHandler.addParameter('disp', 'search2')
        oOutputParameterHandler.addParameter('type', oConfig.getSetting('search2_type'))
        oOutputParameterHandler.addParameter('readdb', 'True')
        sLabel2 = oConfig.getlanguage(30089)+": "+oConfig.getSetting('search2_label')
        oGui.addDir(sSite, 'showSearchText', sLabel2, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('searchtext', sSearchText)
        oOutputParameterHandler.addParameter('disp', 'search3')
        oOutputParameterHandler.addParameter('type', oConfig.getSetting('search3_type'))
        oOutputParameterHandler.addParameter('readdb', 'True')
        sLabel3 = oConfig.getlanguage(30090)+": "+oConfig.getSetting('search3_label')
        oGui.addDir(sSite, 'showSearchText', sLabel3, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('searchtext', sSearchText)
        oOutputParameterHandler.addParameter('disp', 'search4')
        oOutputParameterHandler.addParameter('type', oConfig.getSetting('search4_type'))
        oOutputParameterHandler.addParameter('readdb', 'True')
        sLabel4 = oConfig.getlanguage(30091)+": "+oConfig.getSetting('search4_label')
        oGui.addDir(sSite, 'showSearchText', sLabel4, 'search.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        # oOutputParameterHandler.addParameter('searchtext', sSearchText)
        # oOutputParameterHandler.addParameter('disp', 'search5')
        # oOutputParameterHandler.addParameter('type', '')
        # oOutputParameterHandler.addParameter('readdb', 'True')
        # sLabel5 = ('%s: %s') % (oConfig.getlanguage(30076), oConfig.getlanguage(30092))
        # oGui.addDir('globalSearch', 'searchMovie', sLabel5, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
        oOutputParameterHandler.addParameter('searchtext', sSearchText)
        oOutputParameterHandler.addParameter('disp', 'search10')
        oOutputParameterHandler.addParameter('readdb', 'True')
        oGui.addDir(sSite, 'showSearchText', '[COLOR orange]Recherche: Alluc_ee[/COLOR]', 'search.png', oOutputParameterHandler)

        #history
        if (oConfig.getSetting("history-view") == 'true'):

            row = cDb().get_history()
            if row:
                oGui.addText(SITE_IDENTIFIER, "[COLOR azure]Votre Historique[/COLOR]")
            for match in row:
                oOutputParameterHandler = cOutputParameterHandler()

                #code to get type with disp
                type = oConfig.getSetting('search' + match[2][-1:] + '_type')
                if type:
                    oOutputParameterHandler.addParameter('type', type)
                    xbmcgui.Window(10101).setProperty('search_type', type)

                oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                oOutputParameterHandler.addParameter('searchtext', match[1])
                oOutputParameterHandler.addParameter('disp', match[2])
                oOutputParameterHandler.addParameter('readdb', 'False')


                oGuiElement = cGuiElement()
                oGuiElement.setSiteName('globalSearch')
                oGuiElement.setFunction('searchMovie')
                oGuiElement.setTitle("- "+match[1])
                oGuiElement.setFileName(match[1])
                oGuiElement.setIcon("search.png")
                oGui.CreateSimpleMenu(oGuiElement,oOutputParameterHandler,SITE_IDENTIFIER,'cHome','delSearch', oConfig.getlanguage(30412))
                oGui.addFolder(oGuiElement, oOutputParameterHandler)

            if row:

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                oGui.addDir(SITE_IDENTIFIER, 'delSearch', oConfig.getlanguage(30413), 'search.png', oOutputParameterHandler)


        oGui.setEndOfDirectory()

    def searchMovie2(self):
        oInputParameterHandler = cInputParameterHandler()
        sDisp = oInputParameterHandler.getValue('disp')
        oHandler = cRechercheHandler()
        liste = oHandler.getAvailablePlugins(sDisp)
        self.__callsearch(liste, sDisp)

    def delSearch(self):
        cDb().del_history()
        return True


    def callpluging(self):
        oGui = cGui()

        oInputParameterHandler = cInputParameterHandler()
        sSiteUrl = oInputParameterHandler.getValue('siteUrl')

        oPluginHandler = cSiteHandler()
        aPlugins = oPluginHandler.getAvailablePlugins(sSiteUrl)
        for aPlugin in aPlugins:
            try:
                #exec "import "+aPlugin[1]
                #exec "sSiteUrl = "+aPlugin[1]+"."+sVar
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', aPlugin[0])
                icon = 'sites/%s.png' % (aPlugin[2])
                oGui.addDir(aPlugin[2], aPlugin[3], aPlugin[1], icon, oOutputParameterHandler)
            except:
                pass

        oGui.setEndOfDirectory()

    #plus utiliser depuis le 16/03/2017
    def __callpluging(self, sVar, sIcon):
        oGui = cGui()
        oPluginHandler = cSiteHandler()
        aPlugins = oPluginHandler.getAvailablePlugins(sVar)
        for aPlugin in aPlugins:
            try:
                #exec "import "+aPlugin[1]
                #exec "sSiteUrl = "+aPlugin[1]+"."+sVar
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', aPlugin[0])
                icon = 'sites/%s.png' % (aPlugin[2])
                oGui.addDir(aPlugin[2], aPlugin[3], aPlugin[1], icon, oOutputParameterHandler)
            except:
                pass

        oGui.setEndOfDirectory()

    def searchMovie(self):
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('searchtext')
        sReadDB = oInputParameterHandler.getValue('readdb')
        sDisp = oInputParameterHandler.getValue('disp')

        oHandler = cRechercheHandler()
        oHandler.setText(sSearchText)
        oHandler.setDisp(sDisp)
        oHandler.setRead(sReadDB)
        aPlugins = oHandler.getAvailablePlugins()

        oGui.setEndOfDirectory()