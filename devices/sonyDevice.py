import re
from devices.device import baseDevice
from devices.device import afFace
from devices.device import afPointUsed
from devices.device import afFocusLocation
from devices.device import afFocusLocationFaceTracking

class sonyDevice(baseDevice):
    def __init__ (self, metaData, im):
        super().__init__()
        self.cameraMake = metaData['EXIF:Make']
        self.cameraModel = metaData['EXIF:Model']
        self.metaData = metaData
        self.im = im    
        self.focusPoints = None
        self.focusPointsUsed = None
        self.focusPointsInFocus = None
        self.facesFound = None
        self.allPoints = None
    #end if

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

    def getFaces(self):
        lfaces = []
        if 'MakerNotes:FacesDetected' in self.metaData:
            facesCount = self.metaData.get('MakerNotes:FacesDetected')
            if facesCount > 0:
                for i in range (1, facesCount + 1):
                    key = 'MakerNotes:Face' + str(i) + 'Position'
                    if key in self.metaData:
                        face_coord = self.metaData.get(key)
                        l = list(face_coord.split())
                        l = list(map(float, l))
                        pt = afFace(l[1], l[0], l[2], l[3],'Face ' + str(i))
                        lfaces.append(pt)
                    #end if
                #end for
            #end if
        #end if
        return lfaces
    #end def
