from devices.device import afRect
from devices.device import afPointUsed
from devices.device import afPointInFocus
from devices.device import afPointSelected
from devices.device import afPointPos
from devices.sonyDevice import sonyDevice

_pointPositions = {
# CENTER AF POINTS
    # 7th group
    'E6': [-0.5,    0, -0.5,   0], 'E6 Center': [-0.5,    0, -0.5,   0], 'E6 Center Vertical': [-0.5,    0, -0.5,   0], 'E6 Center F2.8': [-0.5,    0, -0.5,   0],
    'D6': [-0.5,    0, -0.5,  -1],
    'F6': [-0.5,    0, -0.5,   1],
    'C6': [-0.5,    0, -0.5,  -2], 'C6 Vertical': [-0.5,    0, -0.5,  -2],
    'G6': [-0.5,    0, -0.5,   2], 'G6 Vertical': [-0.5,    0, -0.5,   2],
    'B6': [-0.5,    0, -0.5,  -3],
    'H6': [-0.5,    0, -0.5,   3],
    'A6': [-0.5,    0, -0.5,  -4], 'A6 Vertical': [-0.5,    0, -0.5,  -4],
    'I6': [-0.5,    0, -0.5,   4], 'I6 Vertical': [-0.5,    0, -0.5,   4],
    # 5th group
    'E5': [-0.5,   -1, -0.5,   0], 'E5 Vertical': [-0.5,   -1, -0.5,   0],
    'D5': [-0.5,   -1, -0.5,  -1],
    'F5': [-0.5,   -1, -0.5,   1],
    'C5': [-0.5,   -1, -0.5,  -2], 'C5 Vertical': [-0.5,   -1, -0.5,  -2],
    'G5': [-0.5,   -1, -0.5,   2], 'G5 Vertical': [-0.5,   -1, -0.5,   2],
    'B5': [-0.5,   -1, -0.5,  -3],
    'H5': [-0.5,   -1, -0.5,   3],
    'A5': [-0.5,   -1, -0.5,  -4], 'A5 Vertical': [-0.5,   -1, -0.5,  -4],
    'I5': [-0.5,   -1, -0.5,   4], 'I5 Vertical': [-0.5,   -1, -0.5,   4],
    # 7th group
    'E7': [-0.5,    1, -0.5,   0], 'E7 Vertical': [-0.5,    1, -0.5,   0],
    'D7': [-0.5,    1, -0.5,  -1],
    'F7': [-0.5,    1, -0.5,   1],
    'C7': [-0.5,    1, -0.5,  -2], 'C7 Vertical': [-0.5,    1, -0.5,  -2],
    'G7': [-0.5,    1, -0.5,   2], 'G7 Vertical': [-0.5,    1, -0.5,   2],
    'B7': [-0.5,    1, -0.5,  -3],
    'H7': [-0.5,    1, -0.5,   3],
    'A7': [-0.5,    1, -0.5,  -4], 'A7 Vertical': [-0.5,    1, -0.5,  -4],
    'I7': [-0.5,    1, -0.5,   4], 'I7 Vertical': [-0.5,    1, -0.5,   4],
# LEFT PART
    # 4th group
    'E4': [-0.5, -2.8, -0.5,   0],
    'D4': [-0.5, -2.8, -0.5,  -1],
    'F4': [-0.5, -2.8, -0.5,   1],
    'C4': [-0.5, -2.8, -0.5,  -2],
    'G4': [-0.5, -2.8, -0.5,   2],
    'B4': [-0.5, -2.8, -0.5,  -3],
    'H4': [-0.5, -2.8, -0.5,   3],
    # 3rd group
    'E3': [-0.5, -3.7, -0.5,   0],
    'D3': [-0.5, -3.7, -0.5,  -1],
    'F3': [-0.5, -3.7, -0.5,   1],
    'C3': [-0.5, -3.7, -0.5,  -2],
    'G3': [-0.5, -3.7, -0.5,   2],
    'B3': [-0.5, -3.7, -0.5,  -3],
    'H3': [-0.5, -3.7, -0.5,   3],
    # 2nd group
    'E2': [-0.5, -4.6, -0.5,   0],
    'D2': [-0.5, -4.6, -0.5,  -1],
    'F2': [-0.5, -4.6, -0.5,   1],
    'C2': [-0.5, -4.6, -0.5,  -2],
    'G2': [-0.5, -4.6, -0.5,   2],
    'B2': [-0.5, -4.6, -0.5,  -3],
    'H2': [-0.5, -4.6, -0.5,   3],
    # 1st group
    'E1': [-0.5, -5.5, -0.5,   0],
    'D1': [-0.5, -5.5, -0.5,  -1],
    'F1': [-0.5, -5.5, -0.5,   1],
    'C1': [-0.5, -5.5, -0.5,  -2],
    'G1': [-0.5, -5.5, -0.5,   2],
# RIGHT PART
    # 8th group
    'E8':  [-0.5, +2.8, -0.5,   0],
    'D8':  [-0.5, +2.8, -0.5,  -1],
    'F8':  [-0.5, +2.8, -0.5,   1],
    'C8':  [-0.5, +2.8, -0.5,  -2],
    'G8':  [-0.5, +2.8, -0.5,   2],
    'B8':  [-0.5, +2.8, -0.5,  -3],
    'H8':  [-0.5, +2.8, -0.5,   3],
    # 9th group
    'E9':  [-0.5, +3.7, -0.5,   0],
    'D9':  [-0.5, +3.7, -0.5,  -1],
    'F9':  [-0.5, +3.7, -0.5,   1],
    'C9':  [-0.5, +3.7, -0.5,  -2],
    'G9':  [-0.5, +3.7, -0.5,   2],
    'B9':  [-0.5, +3.7, -0.5,  -3],
    'H9':  [-0.5, +3.7, -0.5,   3],
    # 10th group
    'E10': [-0.5, +4.6, -0.5,   0],
    'D10': [-0.5, +4.6, -0.5,  -1],
    'F10': [-0.5, +4.6, -0.5,   1],
    'C10': [-0.5, +4.6, -0.5,  -2],
    'G10': [-0.5, +4.6, -0.5,   2],
    'B10': [-0.5, +4.6, -0.5,  -3],
    'H10': [-0.5, +4.6, -0.5,   3],
    # 11st group
    'E11': [-0.5, +5.5, -0.5,   0],
    'D11': [-0.5, +5.5, -0.5,  -1],
    'F11': [-0.5, +5.5, -0.5,   1],
    'C11': [-0.5, +5.5, -0.5,  -2],
    'G11': [-0.5, +5.5, -0.5,   2],
}

class sonyDevice79PDAF(sonyDevice):
    def __init__ (self, metaData, im):
        super().__init__(metaData, im)
        self.scaleUpdate(im)
        self.focusPoints = self.getAFPoints()
        self.facesFound = self.getFaces()
        self.focusPointsUsed = self.getAFPointsUsed()
        self.focusPointsInFocus = self.getAFPointsInFocus()
        self.focusPointSelected = self.getAFPointSelected()
        self.focusLocation = self.getFocusLocation() 
        self.allPoints = self.focusPoints + self.facesFound + self.focusPointsUsed + self.focusPointsInFocus 
        self.allPoints = self.allPoints + self.focusPointSelected + self.focusLocation

    def getFocusLocation(self):
        return super().getFocusLocation()

    def getAFPointSelected(self):
        """
        Return the AF point selected, None if it is not found
        """
        if 'MakerNotes:AFPointSelected' in self.metaData:
            if self.metaData.get('EXIF:Model') in ('ILCA-77M2','ILCA-68'):
                return [] 
            elif self.metaData.get('EXIF:Model') in ('ILCA-99M2') and 'MakerNotes:AFPointSelected' in self.metaData:
                xp = self.x_c
                yp = self.y_c
                rs = self.r_size
                vspacer = self.vspacer
                hspacer = self.hspacer
                pt = self.metaData.get('MakerNotes:AFPointSelected')
                if pt in _pointPositions:
                    pointSelected = afPointSelected(
                        x=xp+_pointPositions[pt][0]*rs+_pointPositions[pt][1]*hspacer,
                        y=yp+_pointPositions[pt][2]*rs+_pointPositions[pt][3]*vspacer, w=rs)
                    return [pointSelected] 
                else:
                    print("No AF point selected for ", self.metaData.get('EXIF:Model'))
                    return [] 
            else:
                print("No AF point selected for ",self.metaData.get('EXIF:Model'))
                return [] 
        else:
            return [] 
    def getAFPointsUsed(self):
        if 'MakerNotes:AFPointsUsed' not in self.metaData:
            return [] 
        pointsRet = []
        if self.metaData.get('EXIF:Model') in ('ILCA-77M2','ILCA-99M2'):
            afp_used = (self.metaData.get('MakerNotes:AFPointsUsed')).split(', ')
            xp = self.x_c
            yp = self.y_c
            rs = self.r_size
            vspacer = self.vspacer
            hspacer = self.hspacer
            if afp_used:
                for i in range(len(afp_used)):
                    pointsRet.append(afPointUsed(
                        x=xp+_pointPositions[afp_used[i]][0]*rs+_pointPositions[afp_used[i]][1]*hspacer, 
                        y=yp+_pointPositions[afp_used[i]][2]*rs+_pointPositions[afp_used[i]][3]*vspacer, w=rs))
            #endif
        else:
            print("No AF points for ",self.metaData.get('EXIF:Model'))
        return pointsRet

    def getAFPointsInFocus(self):
        if 'MakerNotes:AFPointInFocus' not in self.metaData:
            return [] 
        if 'MakerNotes:AFType' in self.metaData and self.metaData.get('MakerNotes:AFType') in ('79-point'):
            if self.metaData.get('EXIF:Model') in ('ILCA-77M2','ILCA-68'):
                return [] 
            elif self.metaData.get('EXIF:Model') in ('ILCA-99M2'):
                xp = self.x_c
                yp = self.y_c
                rs = self.r_size
                vspacer = self.vspacer
                hspacer = self.hspacer
                pt = self.metaData.get('MakerNotes:AFPointInFocus')
                pointSelected = afPointInFocus(
                    x=xp+_pointPositions[pt][0]*rs+_pointPositions[pt][1]*hspacer + rs/2,
                    y=yp+_pointPositions[pt][2]*rs+_pointPositions[pt][3]*vspacer + rs/2, rad=(0.01*self.xpixels))
                return [pointSelected] 
            else:
                print("No AF point selected for ",self.metaData.get('EXIF:Model'))
                return [] 
        else:
            return [] 

    def getAFPoints(self):
        pointsRet = []
        if self.metaData.get('MakerNotes:AFType') not in ('79-point'):
            return pointsRet

        if self.metaData.get('EXIF:Model') in ('ILCA-77M2','ILCA-99M2'):
            afp_used = (self.metaData.get('MakerNotes:AFPointsUsed')).split(', ')
            xp = self.x_c
            yp = self.y_c
            rs = self.r_size
            vspacer = self.vspacer
            hspacer = self.hspacer
            for key, value in _pointPositions.items():
                if key not in afp_used:
                    pointsRet.append(afPointPos(
                        x=xp+value[0]*rs+value[1]*hspacer, 
                        y=yp+value[2]*rs+value[3]*vspacer, w=rs))
        else:
            print("No AF points for ",self.metaData.get('EXIF:Model'))
        return pointsRet
    #end def

    def scaleUpdate(self, im):
        super().scaleUpdate(im)
        if self.metaData.get('EXIF:Model') == 'ILCA-99M2':
            self.r_size = 0.020*self.xpixels
            self.vspacer = 1.2*self.r_size
            self.hspacer = 2.2*self.r_size
        elif self.metaData.get('EXIF:Model') in ('ILCA-77M2'):
            self.r_size = 0.020*self.xpixels*1.5
            self.vspacer = 1.2*self.r_size
            self.hspacer = 2.2*self.r_size
        else: 
            print("No scale update for ",self.metaData.get('EXIF:Model'))
        #endif
    #end def