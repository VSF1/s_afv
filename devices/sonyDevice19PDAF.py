from devices.device import afRect
from devices.device import afPointUsed
from devices.device import afPointInFocus
from devices.device import afPointPos
from devices.device import afFace
from devices.sonyDevice import sonyDevice
 
class sonyDevice19PDAF(sonyDevice):
    def __init__ (self, metaData, im):
        super().__init__(metaData, im)
        self.scaleUpdate(im)
        self.focusPoints = self.getAFPoints()
        self.facesFound = self.getFaces()
        self.focusPointsUsed = self.getAFPointsUsed()
        self.focusPointsInFocus = self.getAFPointsInFocus()
        self.allPoints = self.focusPoints + self.facesFound + self.focusPointsUsed + self.focusPointsInFocus

    def getAFPointSelected(self):
        if 'EXIF:Model' in self.metaData:
            if self.metaData.get('Exif:Model') in ('SLT-A99'):
                return None
        return None

    def getAFPointsUsed(self):
        if 'MakerNotes:AFType' in self.metaData       and self.metaData.get('MakerNotes:AFType') in ('19-point'):
            return []
        else:
            return []

    def getAFPointsInFocus(self):
        if 'MakerNotes:AFType' in self.metaData and self.metaData.get('MakerNotes:AFType') in ('19-point'):
            return []
        else:
            return []

    def getAFPoints(self):
        if self.metaData.get('MakerNotes:AFType') not in ('19-point'):
            return []
        pointsRet = []
        return pointsRet
    #end def

    def scaleUpdate(self, im):
        super().scaleUpdate(im)
        if self.metaData.get('EXIF:Model') in ('SLT-A99', 'SLT-A99V'):
            self.r_size = 0.039*self.xpixels/1.5
            self.spacer = 0.47*self.xpixels/1.5
            self.rad = 0.03*self.xpixels/1.5
        else: 
            print("No scale update for ",self.metaData.get('EXIF:Model'))
        #endif
    #end def