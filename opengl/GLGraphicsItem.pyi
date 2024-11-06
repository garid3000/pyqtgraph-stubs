from OpenGL.GL import *
from .. import Transform3D as Transform3D
from ..Qt import QtCore as QtCore
from _typeshed import Incomplete

GLOptions: Incomplete

class GLGraphicsItem(QtCore.QObject):
    def __init__(self, parentItem: GLGraphicsItem = None) -> None: ...
    def setParentItem(self, item) -> None:
        """Set this item's parent in the scenegraph hierarchy."""
    def setGLOptions(self, opts: str) -> None:
        """
        Set the OpenGL state options to use immediately before drawing this item.
        (Note that subclasses must call setupGLState before painting for this to work)
        
        The simplest way to invoke this method is to pass in the name of
        a predefined set of options (see the GLOptions variable):
        
        ============= ======================================================
        opaque        Enables depth testing and disables blending
        translucent   Enables depth testing and blending
                      Elements must be drawn sorted back-to-front for
                      translucency to work correctly.
        additive      Disables depth testing, enables blending.
                      Colors are added together, so sorting is not required.
        ============= ======================================================
        
        It is also possible to specify any arbitrary settings as a dictionary. 
        This may consist of {'functionName': (args...)} pairs where functionName must 
        be a callable attribute of OpenGL.GL, or {GL_STATE_VAR: bool} pairs 
        which will be interpreted as calls to glEnable or glDisable(GL_STATE_VAR).
        
        For example::
            
            {
                GL_ALPHA_TEST: True,
                GL_CULL_FACE: False,
                'glBlendFunc': (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA),
            }
            
        
        """
    def updateGLOptions(self, opts) -> None:
        """
        Modify the OpenGL state options to use immediately before drawing this item.
        *opts* must be a dictionary as specified by setGLOptions.
        Values may also be None, in which case the key will be ignored.
        """
    def parentItem(self):
        """Return a this item's parent in the scenegraph hierarchy."""
    def childItems(self):
        """Return a list of this item's children in the scenegraph hierarchy."""
    def view(self): ...
    def setDepthValue(self, value) -> None:
        """
        Sets the depth value of this item. Default is 0.
        This controls the order in which items are drawn--those with a greater depth value will be drawn later.
        Items with negative depth values are drawn before their parent.
        (This is analogous to QGraphicsItem.zValue)
        The depthValue does NOT affect the position of the item or the values it imparts to the GL depth buffer.
        """
    def depthValue(self):
        """Return the depth value of this item. See setDepthValue for more information."""
    def setTransform(self, tr) -> None:
        """Set the local transform for this object.

        Parameters
        ----------
        tr : pyqtgraph.Transform3D
            Tranformation from the local coordinate system to the parent's.
        """
    def resetTransform(self) -> None:
        """Reset this item's transform to an identity transformation."""
    def applyTransform(self, tr, local) -> None:
        """
        Multiply this object's transform by *tr*. 
        If local is True, then *tr* is multiplied on the right of the current transform::
        
            newTransform = transform * tr
            
        If local is False, then *tr* is instead multiplied on the left::
        
            newTransform = tr * transform
        """
    def transform(self):
        """Return this item's transform object."""
    def viewTransform(self):
        """Return the transform mapping this item's local coordinate system to the 
        view coordinate system."""
    def translate(self, dx:float, dy:float, dz:float, local: bool = False) -> None:
        """
        Translate the object by (*dx*, *dy*, *dz*) in its parent's coordinate system.
        If *local* is True, then translation takes place in local coordinates.
        """
    def rotate(self, angle, x, y, z, local: bool = False) -> None:
        """
        Rotate the object around the axis specified by (x,y,z).
        *angle* is in degrees.
        
        """
    def scale(self, x, y, z, local: bool = True) -> None:
        """
        Scale the object by (*dx*, *dy*, *dz*) in its local coordinate system.
        If *local* is False, then scale takes place in the parent's coordinates.
        """
    def hide(self) -> None:
        """Hide this item. 
        This is equivalent to setVisible(False)."""
    def show(self) -> None:
        """Make this item visible if it was previously hidden.
        This is equivalent to setVisible(True)."""
    def setVisible(self, vis) -> None:
        """Set the visibility of this item."""
    def visible(self):
        """Return True if the item is currently set to be visible.
        Note that this does not guarantee that the item actually appears in the
        view, as it may be obscured or outside of the current view area."""
    def initialize(self) -> None: ...
    def isInitialized(self): ...
    def initializeGL(self) -> None:
        """
        Called after an item is added to a GLViewWidget. 
        The widget's GL context is made current before this method is called.
        (So this would be an appropriate time to generate lists, upload textures, etc.)
        """
    def setupGLState(self) -> None:
        """
        This method is responsible for preparing the GL state options needed to render 
        this item (blending, depth testing, etc). The method is called immediately before painting the item.
        """
    def paint(self) -> None:
        """
        Called by the GLViewWidget to draw this item.
        It is the responsibility of the item to set up its own modelview matrix,
        but the caller will take care of pushing/popping.
        """
    def update(self) -> None:
        """
        Indicates that this item needs to be redrawn, and schedules an update 
        with the view it is displayed in.
        """
    def mapToParent(self, point): ...
    def mapFromParent(self, point): ...
    def mapToView(self, point): ...
    def mapFromView(self, point): ...
