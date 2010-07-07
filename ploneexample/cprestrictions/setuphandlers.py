from Products.CMFCore.utils import getToolByName

def setupGroups(context):
    """Setup groups for manager roles."""
    if context.readDataFile('ptrestrictions.setupGroups.txt') is None:
        return
    portal = context.getSite()
    acl_users = getToolByName(portal, 'acl_users')
    gtool = getToolByName(portal, 'portal_groups')
    if not acl_users.searchGroups(name='Administrative Managers'):
        gtool.addGroup('Administrative Managers', roles=['Administrative Manager'])

def editAction(controlpanel, id_, **kwargs):
    cp = controlpanel
    for action in cp.listActions():
        if action.id == id_:
            action.edit(**kwargs)

def setupControlPanel(context):
    """Setup control panel roles."""
    if context.readDataFile('ptrestrictions.setupControlPanel.txt') is None:
        return
    portal = context.getSite()
    cp  = getToolByName(portal, 'portal_controlpanel')
    editAction(cp, 'CalendarSettings', permissions=('Manage the site administratively',))
    editAction(cp, 'HtmlFilter', permissions=('Manage the site administratively',))
    editAction(cp, 'MailHost', permissions=('Manage the site administratively',))
    editAction(cp, 'MarkupSettings', permissions=('Manage the site administratively',))
    editAction(cp, 'SearchSettings', permissions=('Manage the site administratively',))
    editAction(cp, 'SecuritySettings', permissions=('Manage the site administratively',))
    editAction(cp, 'PloneReconfig', permissions=('Manage the site administratively',))
    editAction(cp, 'PortalSkin', permissions=('Manage the site administratively',))
    editAction(cp, 'TypesSettings', permissions=('Manage the site administratively',))
    editAction(cp, 'ContentRules', permissions=('Manage the site administratively',))
