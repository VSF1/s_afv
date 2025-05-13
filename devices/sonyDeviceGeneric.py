import re
from devices.device import afRect
from devices.device import afPointUsed
from devices.device import afPointInFocus
from devices.device import afFocusLocation
from devices.device import afFocusLocationFaceTracking
from devices.device import afFace
from devices.sonyDevice import sonyDevice

class sonyDeviceGeneric(sonyDevice):
    def __init__ (self, metaData, im):
        super().__init__(metaData, im)
        self.scaleUpdate(im)
        self.focusPoints = self.getAFPoints()
        self.facesFound = self.getFaces()
        self.focusPointsUsed = self.getAFPointsUsed()
        self.focusPointsInFocus = self.getAFPointsInFocus()
        self.focusLocation = self.getFocusLocation() 
        self.focusPointSelected = self.getAFPointSelected()
        self.allPoints = self.focusPoints + self.facesFound + self.focusPointsUsed + self.focusPointsInFocus 
        self.allPoints = self.allPoints + self.focusPointSelected + self.focusLocation

    def getAFPoints(self):
        return []
    
    def getAFPointSelected(self):
        return []
    
    def getAFPointsUsed(self):
        return []

    def getAFPointsInFocus(self):
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

    def facesDetected(self):
        if 'MakerNotes:FacesDetected' in self.metaData:
            facesCount = self.metaData.get('MakerNotes:FacesDetected')
            if facesCount > 0:
                return True
            else:
                return False
        return False

    def getFaces(self):
        retfaces = []
        if 'MakerNotes:FacesDetected' in self.metaData:
            facesCount = self.metaData.get('MakerNotes:FacesDetected')
            if facesCount > 0:
                for i in range (1,facesCount):
                    key = 'MakerNotes:Face'+str(i)+'Position'
                    if key in self.metaData:
                        face_coord = self.metaData.get(key)
                        coord = list(face_coord.split())
                        coord = list(map(float, coord))
                        w = coord[2]
                        h = coord[3]
                        x = coord[1]
                        y = coord[0] 
                        pt = afFace(x=x, y=y, w=w, h=h, name='Face '+str(i))
                        retfaces.append(pt)
                    #end if
                #end for
            #end if
        #end if
        return retfaces
    #end def

    def getFocusLocation(self):
        pointRet = []
        if 'MakerNotes:FocusLocation' in self.metaData:
            focusp = self.metaData.get('MakerNotes:FocusLocation')
            focusp = list(focusp.split())
            focusp = list(map(float, focusp))
            if self.metaData.get('MakerNotes:AFAreaMode') == 'Tracking' and self.metaData.get('MakerNotes:AFTracking') == 'Lock On AF' and self.metaData.get('EXIF:Model') in ('ILCE-6400','ILCE-6100','ILCE-6600','ILCE-9','ILCE-7RM4', 'ILCE-7RM4A', 'ILCE-RX100M7', 'ILCE-9M2','ZV-1','ZV-E10','ILCE-1'):
                pointRet = [
                    afPointUsed(x=focusp[2]- 0.01*self.xpixels, y=focusp[3]- 0.02*self.xpixels, w=0.04*self.xpixels),
                    afPointUsed(x=focusp[2]-0.025*self.xpixels, y=focusp[3]-0.025*self.xpixels, w=0.05*self.xpixels)
                ]
            elif self.metaData.get('MakerNotes:AFTracking') == 'Face tracking':
                pointRet = [afFocusLocationFaceTracking(x=focusp[2],y=focusp[3], rad=(0.01*self.xpixels))]
            else:
                pointRet = [afFocusLocation(x=focusp[2],y=focusp[3], rad=(0.01*self.xpixels))]
            #endif
        return pointRet

    def scaleUpdate(self, im):
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
        #endif
    #end def