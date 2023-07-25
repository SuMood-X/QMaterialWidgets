# coding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtDesigner import QDesignerCustomWidgetInterface

from qmaterialwidgets import TimePicker, CalendarPicker

from plugin_base import PluginBase


class DateTimePlugin(PluginBase):

    def group(self):
        return super().group() + ' (Date Time)'


class CalendarPickerPlugin(DateTimePlugin, QDesignerCustomWidgetInterface):
    """ Calendar picker plugin """

    def createWidget(self, parent):
        return CalendarPicker(parent)

    def icon(self):
        return super().icon("CalendarDatePicker")

    def name(self):
        return "CalendarPicker"



class TimePickerPlugin(DateTimePlugin, QDesignerCustomWidgetInterface):
    """ Time picker plugin """

    def createWidget(self, parent):
        return TimePicker(parent)

    def icon(self):
        return super().icon("TimePicker")

    def name(self):
        return "TimePicker"

    def toolTip(self):
        return "24 hours time picker"

