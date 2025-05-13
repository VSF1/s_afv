from devices.sonyDevice79PDAF import sonyDevice79PDAF
from devices.sonyDevice19PDAF import sonyDevice19PDAF
from devices.sonyDevice15PDAF import sonyDevice15PDAF
from devices.sonyDevicePDAF import sonyDevicePDAF
from devices.sonyDeviceGeneric import sonyDeviceGeneric
 
def sonyDeviceFactory(metaData, im):
    if 'MakerNotes:AFType' in metaData:
        if metaData.get('MakerNotes:AFType') in ('79-point'):
            return sonyDevice79PDAF(metaData, im)
        elif metaData.get('MakerNotes:AFType') in ('19-point'):
            return sonyDevice19PDAF(metaData, im)
        if metaData.get('MakerNotes:AFType') in ('15-point'):
            return sonyDevice15PDAF(metaData, im)
        #end if
    else:
        if metaData.get('EXIF:Model') in ('DSLR-A900', 'DSLR-A700', 'DSLR-A850'):
            return sonyDevicePDAF(metaData, im)
        else:
            return sonyDeviceGeneric(metaData, im)
        #end if
    #end if
#end def
