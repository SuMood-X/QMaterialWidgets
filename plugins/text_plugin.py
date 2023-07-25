# coding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtDesigner import QDesignerCustomWidgetInterface

from qmaterialwidgets import (SpinBox, DoubleSpinBox, TextEdit, TimeEdit, DateTimeEdit, LineEdit,
                              DateEdit, SearchLineEdit, FilledSearchLineEdit, FilledLineEdit, FilledTextEdit)

from plugin_base import PluginBase


class TextPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Text)'


class LineEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Line edit plugin """

    def createWidget(self, parent):
        return LineEdit(parent)

    def icon(self):
        return super().icon("TextBox")

    def name(self):
        return "LineEdit"


class FilledLineEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Line edit plugin """

    def createWidget(self, parent):
        return FilledLineEdit(parent)

    def icon(self):
        return super().icon("TextBox")

    def name(self):
        return "FilledLineEdit"


class SearchLineEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Search line edit plugin """

    def createWidget(self, parent):
        return SearchLineEdit(parent)

    def icon(self):
        return super().icon("TextBox")

    def name(self):
        return "SearchLineEdit"


class FilledSearchLineEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Search line edit plugin """

    def createWidget(self, parent):
        return FilledSearchLineEdit(parent)

    def icon(self):
        return super().icon("TextBox")

    def name(self):
        return "FilledSearchLineEdit"


class TextEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Text edit plugin """

    def createWidget(self, parent):
        return TextEdit(parent)

    def icon(self):
        return super().icon("RichEditBox")

    def name(self):
        return "TextEdit"


class FilledTextEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Filled text edit plugin """

    def createWidget(self, parent):
        return FilledTextEdit(parent)

    def icon(self):
        return super().icon("RichEditBox")

    def name(self):
        return "FilledTextEdit"


class DateEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Date edit plugin """

    def createWidget(self, parent):
        return DateEdit(parent)

    def icon(self):
        return super().icon("NumberBox")

    def name(self):
        return "DateEdit"


class TimeEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Time edit plugin """

    def createWidget(self, parent):
        return TimeEdit(parent)

    def icon(self):
        return super().icon("NumberBox")

    def name(self):
        return "TimeEdit"


class DateTimeEditPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Date time edit plugin """

    def createWidget(self, parent):
        return DateTimeEdit(parent)

    def icon(self):
        return super().icon("NumberBox")

    def name(self):
        return "DateTimeEdit"


class SpinBoxPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Spin box plugin """

    def createWidget(self, parent):
        return SpinBox(parent)

    def icon(self):
        return super().icon("NumberBox")

    def name(self):
        return "SpinBox"


class DoubleSpinBoxPlugin(TextPlugin, QDesignerCustomWidgetInterface):
    """ Double spin box plugin """

    def createWidget(self, parent):
        return DoubleSpinBox(parent)

    def icon(self):
        return super().icon("NumberBox")

    def name(self):
        return "DoubleSpinBox"
