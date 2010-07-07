
def initialize(context):
    """Initializer called when used as a Zope 2 product."""

#from Products.CMFCore import permissions as CMFCorePermissions
from AccessControl.SecurityInfo import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

security = ModuleSecurityInfo('ploneexample.cprestrictions')

security.declarePublic('Manage the site administratively')
setDefaultRoles('Manage the site administratively', ())
