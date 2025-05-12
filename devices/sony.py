import re
from devices.device import baseDevice
from devices.device import afRect
from devices.device import afPointUsed
from devices.device import afPointInFocus
from devices.device import afPointPos
from devices.device import afFace
from devices.sonyDevice79PDAF import sonyDevice79PDAF
from devices.sonyDevice19PDAF import sonyDevice19PDAF
from devices.sonyDevice15PDAF import sonyDevice15PDAF
 
def sonyDeviceFactory(metaData, im):
    if 'MakerNotes:AFType' in metaData:
        if metaData.get('MakerNotes:AFType') in ('79-point'):
            return sonyDevice79PDAF(metaData, im)
        elif metaData.get('MakerNotes:AFType') in ('19-point'):
            return sonyDevice19PDAF(metaData, im)
        if metaData.get('MakerNotes:AFType') in ('15-point'):
            return sonyDevice15PDAF(metaData, im)
    else:
        return sonyDevice(metaData, im)

class sonyDevice(baseDevice):
    def __init__ (self, metaData, im):
        self.cameraMake = metaData['EXIF:Make']
        self.cameraModel = metaData['EXIF:Model']
        self.metaData = metaData
        self.__scaleUpdate(im)
        self.focusPoints = self.__getAFPoints()
        self.faces = self.__getFaces()
        self.focusPointsUsed = self.__getAFPointsUsed()
        self.focusPointsInFocus = self.__getAFPointsInFocus()
        self.allPoints = self.focusPoints + self.faces + self.focusPointsUsed + self.focusPointsInFocus

    def __getAFPoints(self):
        if 'MakerNotes:AFType' in self.metaData:
            if self.metaData.get('MakerNotes:AFType') in ('15-point'):
                return self.__getAFPoints15()
            elif self.metaData.get('MakerNotes:AFType') in ('19-point'):
                return []
            elif self.metaData.get('MakerNotes:AFType') in ('79-point'):
                return self.__getAFPoints79()
        else:
            return []
    
    def __getAFPointsUsed(self):
        if 'MakerNotes:AFType' in self.metaData:
            if self.metaData.get('MakerNotes:AFType') in ('15-point'):
                return self.__getAFPointsUsed15()
            elif self.metaData.get('MakerNotes:AFType') in ('19-point'):
                return []
            elif self.metaData.get('MakerNotes:AFType') in ('79-point'):
                return []
        else:
            return []

    def __getAFPointsInFocus(self):
        if 'MakerNotes:AFType' in self.metaData:
            if self.metaData.get('MakerNotes:AFType') in ('15-point'):
                return self.__getAFPointsInFocus15()
            elif self.metaData.get('MakerNotes:AFType') in ('19-point'):
                return []
            elif self.metaData.get('MakerNotes:AFType') in ('79-point'):
                return []
        else:
            return []

    def __getAFPoints15(self):
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

    def __getAFPoints79(self):
        if self.metaData.get('MakerNotes:AFType') not in ('79-point'):
            return []
        pointsRet = []
        if self.metaData.get('EXIF:Model') in ('ILCA-77M2','ILCA-99M2'):
            afp_used = (self.metaData.get('MakerNotes:AFPointsUsed')).split(', ')
            xp = self.x_c # x center
            yp = self.y_c
            rs = self.r_size
            vspacer = self.vspacer
            hspacer = self.hspacer
            # CENTER AF POINTS
            if 'E6' not in afp_used:
                afp = afPointPos(x=xp-rs/2, y=yp-rs/2, w=rs)
                pointsRet.append(afp)
            if 'D6' not in afp_used:
                afp = afPointPos(x=xp-rs/2, y=yp-rs/2-vspacer, w=rs)
                pointsRet.append(afp)
            if 'F6' not in afp_used:
                afp = afPointPos(x=xp-rs/2, y=yp-rs/2+vspacer, w=rs)
                pointsRet.append(afp)
            if 'C6' not in afp_used:
                afp = afPointPos(x=xp-rs/2, y=yp-rs/2+vspacer*2, w=rs)
                pointsRet.append(afp)
            #G6
            '''
            if 'G6' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c+2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c+2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #B6
            if 'B6' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c-3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c-3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #H6
            if 'H6' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c+3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c+3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #A6
            if 'A6' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c-4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
             else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c-4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #I6
            if 'I6' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c+4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2,y_c+4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #E5
            if 'E5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #D5
            if 'D5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #F5
            if 'F5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #C5
            if 'C5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #G5
            if 'G5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #B5
            if 'B5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #H5
            if 'H5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #A5
            if 'A5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c-4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #I5
            if 'I5' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2-hspacer,y_c+4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #E7
            if 'E7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #D7
            if 'D7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #F7
            if 'F7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #C7
            if 'C7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #G7
            if 'G7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+2*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #B7
            if 'B7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #H7
            if 'H7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+3*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #A7
            if 'A7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c-4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            #I7
            if 'I7' in afp_used:
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'limegreen',facecolor='none',alpha =0.9))
            else :
                ax.add_patch(patches.Rectangle((x_c-r_size/2+hspacer,y_c+4*vspacer-r_size/2),r_size,r_size,linewidth=2,edgecolor = 'w',facecolor='none',alpha =0.3))
            '''
        return pointsRet
    #end def
    def __getAFPointsInFocus15(self):
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

    def __getAFPointsUsed15(self):
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

    def __getFaces(self):
        lfaces = []
        if 'MakerNotes:FacesDetected' in self.metaData:
            facesCount = self.metaData.get('MakerNotes:FacesDetected')
            if facesCount > 0:
                for i in range (1,facesCount):
                    key = 'MakerNotes:Face'+str(i)+'Position'
                    if key in self.metaData:
                        face_coord = self.metaData.get(key)
                        l = list(face_coord.split())
                        l = list(map(float, l))
                        pt = afFace(l[1],l[0],l[2],l[3],'Face '+str(i))
                        lfaces.append(pt)
                    #end if
                #end for
            #end if
        #end if
        return lfaces
    #end def

    def __scaleUpdate(self, im):
        self.ypixels, self.xpixels, bands = im.shape
        if self.metaData.get('MakerNotes:FullImageSize'):
            fimsize = re.findall('\\d+', self.metaData.get('MakerNotes:FullImageSize'))
            if int(fimsize[1]) < self.ypixels or int(fimsize[0]) < self.xpixels:
                #debug print ("Crop needed! EXIF Height = ",int(exif.get('Sony Image Height')),", ypixels = ",ypixels)
                xdiff =  int(fimsize[0])
                ydiff =  int(fimsize[1])
                startx = self.xpixels//2-(xdiff//2)
                starty = self.ypixels//2-(ydiff//2)
                im = im[starty:starty+ydiff,startx:startx+xdiff]
                self.ypixels, self.xpixels, bands = im.shape
            #end if
            self.r_size = 0.039*self.xpixels
            self.x_center = self.xpixels/2-self.r_size/2
            self.y_center = self.ypixels/2-self.r_size/2
            self.x_c = self.xpixels/2
            self.y_c = self.ypixels/2
            self.spacer = 0.047*self.xpixels
            self.rad = 0.03*self.xpixels
        if self.metaData.get('EXIF:Model') == 'ILCA-99M2':
            self.r_size = 0.020*self.xpixels
            self.vspacer = 1.2*self.r_size
            self.hspacer = 2.2*self.r_size
        elif self.metaData.get('EXIF:Model') in ('ILCA-77M2'):
            self.r_size = 0.020*self.xpixels*1.5
            self.vspacer = 1.2*self.r_size
            self.hspacer = 2.2*self.r_size
        elif self.metaData.get('EXIF:Model') in ('SLT-A99','SLT-A99V'):
            self.r_size = 0.039*self.xpixels/1.5
            self.spacer = 0.047*self.xpixels/1.5
            self.rad = 0.03*self.xpixels/1.5
        #endif
    #end def