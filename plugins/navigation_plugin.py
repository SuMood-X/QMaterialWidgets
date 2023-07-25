# coding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtDesigner import QDesignerCustomWidgetInterface

from qmaterialwidgets import NavigationRail, NavigationBar, TabWidget, SegmentedWidget, NavigationBar, FluentIcon

from plugin_base import PluginBase


class NavigationPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Navigation)'


class NavigationRailPlugin(NavigationPlugin, QDesignerCustomWidgetInterface):
    """ Navigation rail plugin """

    def createWidget(self, parent):
        return NavigationRail(parent)

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationRail"


class NavigationBarPlugin(NavigationPlugin, QDesignerCustomWidgetInterface):
    """ Navigation abr plugin """

    def createWidget(self, parent):
        return NavigationBar(parent)

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationBar"


class TabWidgetPlugin(NavigationPlugin, QDesignerCustomWidgetInterface):
    """ Tab widget plugin """

    def createWidget(self, parent):
        p = TabWidget(parent)
        for i in range(1, 4):
            p.addItem(f'Item{i}', f'Item{i}', print, FluentIcon.BASKETBALL)

        p.setCurrentItem('Item1')
        return p

    def icon(self):
        return super().icon("TabView")

    def name(self):
        return "TabWidget"

