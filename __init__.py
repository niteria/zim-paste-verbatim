from zim.plugins import PluginClass
from zim.gui.mainwindow import MainWindowExtension
from zim.actions import action


class PasteFromHTMLPlugin(PluginClass):
    plugin_info = {
        "name": _("Paste Verbatim"),
        "description": _("This plugin wraps Paste As Verbatim to be able to bind to a keyboard shortcut"),
        "author": "@niteria",
        "help": "Plugins:Paste Verbatim"
    }
    plugin_preferences = (
    )

class PasteVerbatimExtension(MainWindowExtension):

    def __init__(self, plugin, window):
        MainWindowExtension.__init__(self, plugin, window)
        self.plugin = plugin
    uimanager_xml = '''
    <ui>
    <menubar name='menubar'>
    <menu action='tools_menu'>
    <placeholder name='plugin_items'>
    <menuitem action='pastev'/>
    </placeholder>
    </menu>
    </menubar>
    </ui>
    '''

    @action(_('_Paste Verbatim'), accelerator="<ctrl><shift>v")
    def pastev(self):
        self.window.pageview.textview.do_paste_clipboard(format='verbatim')
