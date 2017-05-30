import ui
import time
import uiScriptLocale
import localeInfo
import net
import dbg
import app
import os
import snd
import wndMgr

app.SetGuildMarkPath("test")

class LogoWindow (ui.ScriptWindow):

	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		self.stream = stream
		self.__LoadLogoAnimation()
	
	def __LoadLogoAnimation(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "IntroLogoWindow.py")
		
		GetObject=self.GetChild
		
		self.img01			= GetObject("img_01")
		self.img02			= GetObject("img_02")
		self.img03			= GetObject("img_03")
		self.img04			= GetObject("img_04")
		self.img05			= GetObject("img_05")
		self.img06			= GetObject("img_06")
		self.img07			= GetObject("img_07")
		self.img08			= GetObject("img_08")
		self.img09			= GetObject("img_09")
		self.img10			= GetObject("img_10")
		self.img11			= GetObject("img_11")
		self.img12			= GetObject("img_12")
		self.img13			= GetObject("img_13")
		self.img14			= GetObject("img_14")
		self.img15			= GetObject("img_15")
		self.img16			= GetObject("img_16")
		self.img17			= GetObject("img_17")
		self.img18			= GetObject("img_18")
		self.img19			= GetObject("img_19")
		self.img20			= GetObject("img_20")
		self.img21			= GetObject("img_21")
		self.img22			= GetObject("img_22")
		self.img23			= GetObject("img_23")
		self.img24			= GetObject("img_24")
		self.img25			= GetObject("img_25")
		self.img26			= GetObject("img_26")
		self.img27			= GetObject("img_27")
		self.img28			= GetObject("img_28")
		self.img29			= GetObject("img_29")
		self.img30			= GetObject("img_30")
		self.img31			= GetObject("img_31")
		self.img32			= GetObject("img_32")
		self.img33			= GetObject("img_33")
		self.img34			= GetObject("img_34")
		self.img35			= GetObject("img_35")
		self.img36			= GetObject("img_36")
		self.img37			= GetObject("img_37")
		self.img38			= GetObject("img_38")
		self.img39			= GetObject("img_39")
		self.img40			= GetObject("img_40")
		self.img41			= GetObject("img_41")
		self.img42			= GetObject("img_42")
		self.img43			= GetObject("img_43")
		self.img44			= GetObject("img_44")
		self.img45			= GetObject("img_45")
		self.img46			= GetObject("img_46")
		self.img47			= GetObject("img_47")
		self.img48			= GetObject("img_48")
		self.img49			= GetObject("img_49")
		self.img50			= GetObject("img_50")

		self.img01.Hide()
		self.img02.Hide()
		self.img03.Hide()
		self.img04.Hide()
		self.img05.Hide()
		self.img06.Hide()
		self.img07.Hide()
		self.img08.Hide()
		self.img09.Hide()
		self.img10.Hide()
		self.img11.Hide()
		self.img12.Hide()
		self.img13.Hide()
		self.img14.Hide()
		self.img15.Hide()
		self.img16.Hide()
		self.img17.Hide()
		self.img18.Hide()
		self.img19.Hide()
		self.img20.Hide()
		self.img21.Hide()
		self.img22.Hide()
		self.img23.Hide()
		self.img24.Hide()
		self.img25.Hide()
		self.img26.Hide()
		self.img27.Hide()
		self.img28.Hide()
		self.img29.Hide()
		self.img30.Hide()
		self.img31.Hide()
		self.img32.Hide()
		self.img33.Hide()
		self.img34.Hide()
		self.img35.Hide()
		self.img36.Hide()
		self.img37.Hide()
		self.img38.Hide()
		self.img39.Hide()
		self.img40.Hide()
		self.img41.Hide()
		self.img42.Hide()
		self.img43.Hide()
		self.img44.Hide()
		self.img45.Hide()
		self.img46.Hide()
		self.img47.Hide()
		self.img48.Hide()
		self.img49.Hide()
		self.img50.Hide()
		
		self.curTime = time.clock()
		self.speedFrame = 0.06
		
	def OnUpdate(self):		
		if ( time.clock() <= self.curTime + self.speedFrame * 2 ):
			self.img02.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 3 and time.clock() > self.curTime + self.speedFrame * 2 ):
			self.img02.Hide()
			self.img03.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 4 and time.clock() > self.curTime + self.speedFrame * 3 ):
			self.img03.Hide()
			self.img04.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 5 and time.clock() > self.curTime + self.speedFrame * 4 ):
			self.img04.Hide()
			self.img05.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 6 and time.clock() > self.curTime + self.speedFrame * 5 ):
			self.img05.Hide()
			self.img06.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 7 and time.clock() > self.curTime + self.speedFrame * 6 ):
			self.img06.Hide()
			self.img07.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 8 and time.clock() > self.curTime + self.speedFrame * 7 ):
			self.img07.Hide()
			self.img08.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 9 and time.clock() > self.curTime + self.speedFrame * 8 ):
			self.img08.Hide()
			self.img09.Show()
			
		if ( time.clock() <= self.curTime + self.speedFrame * 10 and time.clock() > self.curTime + self.speedFrame * 9 ):
			self.img09.Hide()
			self.img10.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 11 and time.clock() > self.curTime + self.speedFrame * 10 ):
			self.img10.Hide()
			self.img11.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 12 and time.clock() > self.curTime + self.speedFrame * 11 ):
			self.img11.Hide()
			self.img12.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 13 and time.clock() > self.curTime + self.speedFrame * 12 ):
			self.img12.Hide()
			self.img13.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 14 and time.clock() > self.curTime + self.speedFrame * 13 ):
			self.img13.Hide()
			self.img14.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 15 and time.clock() > self.curTime + self.speedFrame * 14 ):
			self.img14.Hide()
			self.img15.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 16 and time.clock() > self.curTime + self.speedFrame * 15 ):
			self.img15.Hide()
			self.img16.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 17 and time.clock() > self.curTime + self.speedFrame * 16 ):
			self.img16.Hide()
			self.img17.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 18 and time.clock() > self.curTime + self.speedFrame * 17 ):
			self.img17.Hide()
			self.img18.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 19 and time.clock() > self.curTime + self.speedFrame * 18 ):
			self.img18.Hide()
			self.img19.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 20 and time.clock() > self.curTime + self.speedFrame * 19 ):
			self.img19.Hide()
			self.img20.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 21 and time.clock() > self.curTime + self.speedFrame * 20 ):
			self.img20.Hide()
			self.img21.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 22 and time.clock() > self.curTime + self.speedFrame * 21 ):
			self.img21.Hide()
			self.img22.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 23 and time.clock() > self.curTime + self.speedFrame * 22 ):
			self.img22.Hide()
			self.img23.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 24 and time.clock() > self.curTime + self.speedFrame * 23 ):
			self.img23.Hide()
			self.img24.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 25 and time.clock() > self.curTime + self.speedFrame * 24 ):
			self.img24.Hide()
			self.img25.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 26 and time.clock() > self.curTime + self.speedFrame * 25 ):
			self.img25.Hide()
			self.img26.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 27 and time.clock() > self.curTime + self.speedFrame * 26 ):
			self.img26.Hide()
			self.img27.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 28 and time.clock() > self.curTime + self.speedFrame * 27 ):
			self.img27.Hide()
			self.img28.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 29 and time.clock() > self.curTime + self.speedFrame * 28 ):
			self.img28.Hide()
			self.img29.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 30 and time.clock() > self.curTime + self.speedFrame * 29 ):
			self.img29.Hide()
			self.img30.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 31 and time.clock() > self.curTime + self.speedFrame * 30 ):
			self.img30.Hide()
			self.img31.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 32 and time.clock() > self.curTime + self.speedFrame * 31 ):
			self.img31.Hide()
			self.img32.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 33 and time.clock() > self.curTime + self.speedFrame * 32 ):
			self.img32.Hide()
			self.img33.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 34 and time.clock() > self.curTime + self.speedFrame * 33 ):
			self.img33.Hide()
			self.img34.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 35 and time.clock() > self.curTime + self.speedFrame * 34 ):
			self.img34.Hide()
			self.img35.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 36 and time.clock() > self.curTime + self.speedFrame * 35 ):
			self.img35.Hide()
			self.img36.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 37 and time.clock() > self.curTime + self.speedFrame * 36 ):
			self.img36.Hide()
			self.img37.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 38 and time.clock() > self.curTime + self.speedFrame * 37 ):
			self.img37.Hide()
			self.img38.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 39 and time.clock() > self.curTime + self.speedFrame * 38 ):
			self.img38.Hide()
			self.img39.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 40 and time.clock() > self.curTime + self.speedFrame * 39 ):
			self.img39.Hide()
			self.img40.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 41 and time.clock() > self.curTime + self.speedFrame * 40 ):
			self.img40.Hide()
			self.img41.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 42 and time.clock() > self.curTime + self.speedFrame * 41 ):
			self.img41.Hide()
			self.img42.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 43 and time.clock() > self.curTime + self.speedFrame * 42 ):
			self.img42.Hide()
			self.img43.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 44 and time.clock() > self.curTime + self.speedFrame * 43 ):
			self.img43.Hide()
			self.img44.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 45 and time.clock() > self.curTime + self.speedFrame * 44 ):
			self.img44.Hide()
			self.img45.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 46 and time.clock() > self.curTime + self.speedFrame * 45 ):
			self.img45.Hide()
			self.img46.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 47 and time.clock() > self.curTime + self.speedFrame * 46 ):
			self.img46.Hide()
			self.img47.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 48 and time.clock() > self.curTime + self.speedFrame * 47 ):
			self.img47.Hide()
			self.img48.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 49 and time.clock() > self.curTime + self.speedFrame * 48 ):
			self.img48.Hide()
			self.img49.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 50 and time.clock() > self.curTime + self.speedFrame * 49 ):
			self.img49.Hide()
			self.img50.Show()
		
		if ( time.clock() <= self.curTime + self.speedFrame * 51 and time.clock() > self.curTime + self.speedFrame * 50 ):
			self.img50.Hide()
			self.Hide()
			self.stream.SetLoginPhase()
