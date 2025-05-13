from enum import Enum
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects

def norm(val):
    ret = float(val)
    ret = ret/1000
    if ret > 1:
        ret = 1
    #end if
    ret = 1-ret
    ret = str(ret)
    return ret
#end def

class afPoint (object) :
    def __init__ (self, x, y, name=None) :
        """
        Create a point object.

        Parameters
        ----------
        x : int
            The x location of the point.
        y : int
            The y location of the point.
        pointType : pointType
            The type of point.
        """
        self.x = x
        self.y = y
        self.name = name
    #end def

    def render (self, ax) :
        ax.add_patch(patches.Rectangle((self.x,self.y),self.w,self.h, linewidth = 1,
            edgecolor = self.edgecolor, facecolor = self.facecolor, alpha = 0.9))
        if self.name:
            txt = ax.text(self.x_center, self.y_center, self.name, color='w', weight='bold', fontsize='small',
                ha='center', va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class afRect(afPoint) :
    def __init__ (self, x, y, w, h=None, name=None) :
        afPoint.__init__(self, x, y, name)
        self.w = w
        if h is None:
            self.h = w
        else:
            self.h = h
        #end if
    #end def

    def render (self, ax) :
        if self.name:
            ax.add_patch(patches.Rectangle((self.x, self.y), self.w, self.h, linewidth = 1, edgecolor = "limegreen",
            facecolor = norm(self.name), alpha = 0.9))
            txt = ax.text(self.x_center, self.y_center, self.name, color='w', weight='bold', fontsize='small',
                ha='center', va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth = 2, foreground = 'black'), path_effects.Normal()])
        else:
            ax.add_patch(patches.Rectangle((self.x, self.y), self.w, self.h, linewidth = 1, edgecolor = "limegreen",
                facecolor = 'none', alpha = 0.9))
        #end if
    #end def
#end class

class afPointPos(afRect) :
    def __init__ (self, x, y, w, h=None, name=None) :
        afRect.__init__(self, x, y, w, h, name)
    #end def

    def render (self, ax) :
        if self.name:
            ax.add_patch(patches.Rectangle((self.x,self.y), self.w,self.h, linewidth = 2, edgecolor = 'white',
                facecolor = norm(self.name), alpha = 0.3))
            txt = ax.text(self.x_center, self.y_center, self.name, color='w', weight='bold', fontsize='small',
                ha='center', va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        else:
            ax.add_patch(patches.Rectangle((self.x,self.y), self.w,self.h, linewidth = 2, edgecolor = 'w',
                facecolor = 'none', alpha = 0.3))
        #end if
    #end def
#end class

class afPointUsed(afRect) :
    def __init__ (self, x, y, w, h=None, name = None) :
        afRect.__init__(self, x, y, w, h, name)
    #end def

    def render (self, ax) :
        ax.add_patch(patches.Rectangle((self.x, self.y), self.w, self.h, linewidth = 2, edgecolor = "limegreen",
            facecolor = 'none', alpha = 0.9))
        if self.name:
            txt = ax.text(self.x_center, self.y_center, self.name, color = 'w', weight = 'bold', fontsize = 'small',
                ha = 'center', va = 'center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class afPointInFocus(afPoint) :
    def __init__ (self, x, y, rad, name=None, linewidth=2, edgecolor='yellow') :
        afPoint.__init__(self, x, y, name)
        self.rad = rad
        self.linewidth = linewidth
        self.edgecolor = edgecolor
    #end def

    def render (self, ax):
        ax.add_patch(patches.Circle((self.x,self.y), self.rad, linewidth=self.linewidth,edgecolor = self.edgecolor,facecolor='none',alpha =0.9))
        if self.name:
            txt = ax.text(self.x, self.y, self.name, color='w', weight='bold', fontsize='small', ha='center',
                va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class afFocusLocation(afPoint) :
    def __init__ (self, x, y, rad, name=None) :
        afPoint.__init__(self, x, y, name)
        self.rad = rad
    #end def

    def render (self, ax):
        ax.add_patch(patches.Circle((self.x,self.y), self.rad, linewidth=1, edgecolor = 'yellow', facecolor='none', alpha =0.9))
        if self.name:
            txt = ax.text(self.x, self.y, self.name, color='w', weight='bold', fontsize='small', ha='center',
                va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class afFocusLocationFaceTracking(afPoint) :
    def __init__ (self, x, y, rad, name=None) :
        afPoint.__init__(self, x, y, name)
        self.rad = rad
    #end def

    def render (self, ax):
        ax.add_patch(patches.Circle((self.x,self.y), self.rad, linewidth=1,edgecolor='lime',facecolor='none',alpha =0.9))
        if self.name:
            txt = ax.text(self.x, self.y, self.name, color='w', weight='bold', fontsize='small', ha='center',
                va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class afPointSelected(afPoint) :
    def __init__ (self, x, y, rad, name=None) :
        afPoint.__init__(self, x, y, name)
        self.rad = rad
    #end def

    def render (self, ax):
        ax.add_patch(patches.Circle((self.x,self.y), self.rad, linewidth=2,edgecolor = 'green',facecolor='none',alpha =0.9))
        if self.name:
            txt = ax.text(self.x, self.y, self.name, color='w', weight='bold', fontsize='small', ha='center',
                va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class afFace (afRect) :
    def __init__ (self, x, y, w, h, name):
        afRect.__init__(self, x, y, w, h, name)
    #end def

    def render (self, ax):
        ax.add_patch(patches.Rectangle((self.x,self.y),self.w,self.h, linewidth=1, edgecolor='r', facecolor='none'))
        if self.name:
            txt = ax.text(self.x,self.y,self.name, color='w', weight='bold', fontsize='small', ha='center', va='center')
            txt.set_path_effects([path_effects.Stroke(linewidth=2, foreground='black'), path_effects.Normal()])
        #end if
    #end def
#end class

class baseDevice(object):
    def __init__ (self):
        self.cameraMake = None
        self.cameraModel = None
        self.metaData = None
        self.allPoints = None
    #end def

    def render (self, ax) :
        if self.allPoints:
            for point in self.allPoints:
                if point is not None:
                    point.render(ax)
            #end for
        #end if
    #end def
#end class