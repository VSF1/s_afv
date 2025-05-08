
mn_aftype = {1:"15-point", 2:"19-point", 3:"79-point"}
mn_focusmode = {0:"Manual", 2:"AF-S", 3:"AF-C", 4:"AF-A", 5:"DMF"}
mn_afpoint = {0:"B4"} 
mn_afareamode = {
    0: "Multi",
    1: "Center",
    2: "Spot",
    3: "Flexible Spot",
    10: "Selective (for Miniature effect)",
    11: "Zone",
    12: "Expanded Flexible Spot",
    13: "Custom AF Area",
    14: "Tracking",
    15: "Face Tracking",
    20: "Animal Eye Tracking",
    21: "Human Eye Tracking",
    255: "Manual"
}
mn_aftracking = {0: "Off", 1: "Face tracking", 2: "Lock On AF"}
mn_afstatus = {0: "Not Used", 1: "Used", 2: "Failed", 3: "In Focus"}
mn_afareadmode_slt = {0: "Wide", 4: "Local", 8: "Zone", 9: "Spot"}

def make_exif(exifdata):
    exif = dict()
    for i, tag in enumerate(exifdata):
        value = exifdata[tag]
        if 'MakerNotes:AFType' == tag:
            value = mn_aftype[value]
        elif 'MakerNotes:FocusMode' == tag:
            value = mn_focusmode[value]
        elif 'MakerNotes:AFAreaMode' == tag:
            value = mn_afareamode[value]
        elif 'MakerNotes:AFTracking' == tag:
            value = mn_aftracking[value]
        elif 'MakerNotes:AFStatus' == tag:
            value = mn_afstatus[value]
        exif[tag] = value
    return exif