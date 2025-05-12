from devices.device import afRect
from devices.device import afPointUsed
from devices.device import afPointInFocus
from devices.device import afPointPos
from devices.sonyDevice import sonyDevice
 
class sonyDevice15PDAF(sonyDevice):
    def __init__ (self, metaData, im):
        super().__init__(metaData, im)
        self.metaData = metaData
        self.scaleUpdate(im)
        self.focusPoints = self.getAFPoints()
        self.facesFound = self.getFaces()
        self.focusPointsUsed = self.getAFPointsUsed()
        self.focusPointsInFocus = self.getAFPointsInFocus()
        self.allPoints = self.focusPoints + self.facesFound + self.focusPointsUsed + self.focusPointsInFocus

    def getAFPoints(self):
        if self.metaData.get('MakerNotes:AFType') not in ('15-point'):
            return []
        pointsRet = []
        #end if
        for key in sorted(self.metaData.items()):
            tag = key[0]
            value = key[1]
            afp = None
            if not tag.startswith('MakerNotes:AFStatus'):
                continue
            #endif 
            vl = re.findall('\\d+',value)
            if not vl:
                vl.append('32768')
            #end if
            if tag == 'MakerNotes:AFStatusCenterHorizontal':
                cross_h = int(vl[0])
            elif tag == 'MakerNotes:AFStatusCenterVertical':
                cross_v = int(vl[0])
                if cross_h < cross_v:
                    cross = cross_h
                else:
                    cross = cross_v
                #end if
                cross = str(int(cross))
                afp = afRect(self.x_center, self.y_center, self.r_size, self.r_size, name=cross)
            elif tag == 'MakerNotes:AFStatusBottomHorizontal':
                cross_h = int(vl[0])
            elif tag == 'MakerNotes:AFStatusBottomVertical':
                cross_v = int(vl[0])
                if cross_h < cross_v:
                    cross = cross_h
                else:
                    cross = cross_v
                #end if
                cross = str(int(cross))
                afp = afRect(self.x_center, self.y_center+2*self.spacer, self.r_size, self.r_size, name=cross)
            elif tag == 'MakerNotes:AFStatusTopHorizontal':
                cross_h = int(vl[0])
            elif tag == 'MakerNotes:AFStatusTopVertical':
                cross_v = int(vl[0])
                if cross_h < cross_v:
                    cross = cross_h
                else:
                    cross = cross_v
                #end if
                cross = str(int(cross))
                afp = afRect(self.x_center, self.y_center-2*self.spacer, self.r_size, self.r_size, name=cross)
            elif tag == 'MakerNotes:AFStatusLower-middle':
                afp = afRect(self.x_center, self.y_center+self.spacer, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusUpper-middle':
                afp = afRect(self.x_center, self.y_center-self.spacer, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusNearLeft':
                afp = afRect(self.x_center-self.spacer, self.y_center, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusLeft':
                afp = afRect(self.x_center-3.5*self.spacer, self.y_center, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusRight':
                afp = afRect(self.x_center+3.5*self.spacer, self.y_center, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusFarLeft':
                afp = afRect(self.x_center-5*self.spacer, self.y_center, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusFarRight':
                afp = afRect(self.x_center+5*self.spacer, self.y_center, self.r_size, self.r_size, name=vl[0])
            elif tag == 'Maker:AFStatusLower-left':
                afp = afRect(self.x_center-3.5*self.spacer, self.y_center+1.6*self.spacer, self.r_size, self.r_size,
                    name=vl[0])
            elif tag == 'Maker:AFStatusLower-right':
                afp = afRect(self.x_center+3.5*self.spacer, self.y_center+1.6*self.spacer, self.r_size, self.r_size,
                    name=vl[0])
            elif tag == 'Maker:AFStatusUpper-left':
                afp = afRect(self.x_center-3.5*self.spacer, self.y_center-1.6*self.spacer, self.r_size, self.r_size,
                    name=vl[0])
            elif tag == 'Maker:AFStatusUpper-right':
                afp = afRect(self.x_center+3.5*self.spacer, self.y_center-1.6*self.spacer, self.r_size, self.r_size,
                    name=vl[0])
            #end if
            if afp is not None:
                pointsRet.append(afp)
            #end if
        #end for
        return pointsRet
    #end def

    def getAFPointsInFocus(self):
        pointsRet = []
        if 'MakerNotes:AFPointInFocus' in self.metaData:
            afif = self.metaData.get('MakerNotes:AFPointInFocus')
            if afif in ('Center (vertical)', 'Center (horizontal)'):
                afp = afPointInFocus(self.x_c, self.y_c, self.rad)
            elif afif in ('Bottom (vertical)', 'Bottom (horizontal)'):
                afp = afPointInFocus(self.x_c, self.y_c+2*self.spacer, self.rad)
            elif afif in ('Top (vertical)' , 'Top (horizontal)'):
                afp = afPointInFocus(self.x_c, self.y_c-2*self.spacer, self.rad)
            elif afif == 'Near Left':
                afp = afPointInFocus(self.x_c-self.spacer, self.y_c, self.rad)
            elif afif == 'Near Right':
                afp = afPointInFocus(self.x_c+self.spacer, self.y_c, self.rad)
            elif afif == 'Left':
                afp = afPointInFocus(self.x_c-3.5*self.spacer, self.y_c, self.rad)
            elif afif == 'Right':
                afp = afPointInFocus(self.x_c+3.5*self.spacer, self.y_c, self.rad)
            elif afif == 'Lower-middle':
                afp = afPointInFocus(self.x_c, self.y_c+self.spacer, self.rad)
            elif afif == 'Upper-middle':
                afp = afPointInFocus(self.x_c, self.y_c-self.spacer, self.rad)
            elif afif == 'Lower-left':
                afp = afPointInFocus(self.x_c-3.5*self.spacer, self.y_c+1.6*self.spacer, self.rad)
            elif afif == 'Lower-right' :
                afp = afPointInFocus(self.x_c+3.5*self.spacer, self.y_c+1.6*self.spacer, self.rad)
            elif afif == 'Upper-left' :
                afp = afPointInFocus(self.x_c-3.5*self.spacer, self.y_c-1.6*self.spacer, self.rad)
            elif afif == 'Upper-right' :
                afp = afPointInFocus(self.x_c+3.5*self.spacer, self.y_c-1.6*self.spacer, self.rad)
            elif afif == 'Far Left' :
                afp = afPointInFocus(self.x_c-5*self.spacer, self.y_c, self.rad)
            elif afif == 'Far Right' :
                afp = afRect(self.x_c+5*self.spacer, self.y_c, self.rad)
            else:
                afp = None
            if afp is not None:
                pointsRet.append(afp)
        #end if
        return pointsRet
    #end def

    def getAFPointsUsed(self):
        pointsRet = []
        if 'MakerNotes:AFPointsUsed' in (self.metaData) and self.metaData["MakerNotes:AFPointsUsed"] != '(none)':
            afp_used = list((self.metaData.get('MakerNotes:AFPointsUsed')).split(', '))
            for i, afif in enumerate(afp_used) :
                if afif == 'Center':
                    afp = afPointUsed(self.x_center, self.y_center, self.r_size, self.r_size)
                elif afif == 'Bottom' :
                    afp = afPointUsed(self.x_center, self.y_center + 2*self.spacer, self.r_size, self.r_size)
                elif afif == 'Top' :
                    afp = afPointUsed(self.x_center, self.y_center-2*self.spacer, self.r_size, self.r_size)
                elif afif == 'Near Left' :
                    afp = afPointUsed(self.x_center-self.spacer, self.y_center, self.r_size, self.r_size)
                elif afp_used[i] == 'Near Right' :
                    afp = afPointUsed(self.x_center+self.spacer, self.y_center, self.r_size, self.r_size)
                elif afp_used[i] == 'Left' :
                    afp = afPointUsed(self.x_center-3,5*self.spacer, self.y_center, self.r_size, self.r_size)
                elif afp_used[i] == 'Right' :
                    afp = afPointUsed(self.x_center+3,5*self.spacer, self.y_center, self.r_size, self.r_size)
                elif afp_used[i] == 'Lower-middle' :
                    afp = afPointUsed(self.x_center, self.y_center+self.spacer, self.r_size, self.r_size)
                elif afp_used[i] == 'Upper-middle' :
                    afp = afPointUsed(self.x_center, self.y_center-self.spacer, self.r_size, self.r_size)
                elif afp_used[i] == 'Far Left' :
                    afp = afPointUsed(self.x_center-5*self.spacer, self.y_center, self.r_size, self.r_size)
                elif afp_used[i] == 'Far Right' :
                    afp = afPointUsed(self.x_center+5*self.spacer, self.y_center, self.r_size, self.r_size)
                elif afp_used[i] == 'Lower-left' :
                    afp = afPointUsed(self.x_center-3.5*self.spacer, self.y_center+1.6*self.spacer, self.r_size, self.r_size)
                elif afp_used[i] == 'Lower-right' :
                    afp = afPointUsed(self.x_center+3.5*self.spacer, self.y_center+1.6*self.spacer, self.r_size, self.r_size)
                elif afp_used[i] == 'Upper-left' :
                    afp = afPointUsed(self.x_center-3.5*self.spacer, self.y_center-1.6*self.spacer, self.r_size, self.r_size)
                elif afp_used[i] == 'Upper-right' :
                    afp = afPointUsed(self.x_center+3.5*self.spacer, self.y_center-1.6*self.spacer, self.r_size, self.r_size)
                else:
                    afp = None
                #end if
                if afp is not None:
                    pointsRet.append(afp)
                #end if
        #end if
        return pointsRet
    #end def

    def scaleUpdate(self, im):
        super().scaleUpdate(im)
    #end def
#end class