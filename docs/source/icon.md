## Icon
Many widgets need icons, if you want QMaterialWidgets change your icons automatically when the theme changes, then you can inherit `MaterialIconBase` and overide `path()` method. Here is an example:

```python
from enum import Enum

from qmaterialwidgets import getIconColor, Theme, MaterialIconBase


class MyFluentIcon(MaterialIconBase, Enum):
    """ Custom icons """

    ADD = "Add"
    CUT = "Cut"
    COPY = "Copy"

    def path(self, theme=Theme.AUTO):
        return f':/icons/{self.value}_{getIconColor(theme)}.svg'
```