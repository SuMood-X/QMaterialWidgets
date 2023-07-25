# /**
#  * @license
#  * Copyright 2021 Google LLC
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *      http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  */

from ..palettes.core_palette import *
import json

# /**
#  * Represents a Material color scheme, a mapping of color roles to colors.
#  */
# Using dictionary instead of JavaScript Object
class Scheme:
    def __init__(self, props):
        self.props = props

    @property
    def primary(self):
        return self.props["primary"]

    @property
    def onPrimary(self):
        return self.props["onPrimary"]

    @property
    def primaryContainer(self):
        return self.props["primaryContainer"]

    @property
    def onPrimaryContainer(self):
        return self.props["onPrimaryContainer"]

    @property
    def secondary(self):
        return self.props["secondary"]

    @property
    def secondaryContainer(self):
        return self.props["secondaryContainer"]

    @property
    def onSecondary(self):
        return self.props["onSecondary"]

    @property
    def onSecondaryContainer(self):
        return self.props["onSecondaryContainer"]

    @property
    def tertiary(self):
        return self.props["tertiary"]

    @property
    def onTertiary(self):
        return self.props["onTertiary"]

    @property
    def tertiaryContainer(self):
        return self.props["tertiaryContainer"]

    @property
    def onTertiaryContainer(self):
        return self.props["onTertiaryContainer"]

    @property
    def error(self):
        return self.props["error"]

    @property
    def onError(self):
        return self.props["onError"]

    @property
    def errorContainer(self):
        return self.props["errorContainer"]

    @property
    def onErrorContainer(self):
        return self.props["onErrorContainer"]

    @property
    def background(self):
        return self.props["background"]

    @property
    def onBackground(self):
        return self.props["onBackground"]

    @property
    def surface(self):
        return self.props["surface"]

    @property
    def surfaceBright(self):
        return self.props["surfaceBright"]

    @property
    def onSurface(self):
        return self.props["onSurface"]

    @property
    def surfaceContainerHigh(self):
        return self.props["surfaceContainerHigh"]

    @property
    def surfaceContainer(self):
        return self.props["surfaceContainer"]

    @property
    def surfaceContainerLow(self):
        return self.props["surfaceContainerLow"]

    @property
    def surfaceContainerHighest(self):
        return self.props["surfaceContainerHighest"]

    @property
    def surfaceVariant(self):
        return self.props["surfaceVariant"]

    @property
    def onSurfaceVariant(self):
        return self.props["onSurfaceVariant"]

    @property
    def outline(self):
        return self.props["outline"]

    @property
    def outlineVariant(self):
        return self.props["outlineVariant"]

    @property
    def shadow(self):
        return self.props["shadow"]

    @property
    def inverseSurface(self):
        return self.props["inverseSurface"]

    @property
    def inverseOnSurface(self):
        return self.props["inverseOnSurface"]

    @property
    def inversePrimary(self):
        return self.props["inversePrimary"]

    # /**
    #  * @param argb ARGB representation of a color.
    #  * @return Light Material color scheme, based on the color's hue.
    #  */
    @staticmethod
    def light(argb):
        core = CorePalette.of(argb)
        return Scheme({
            "primary" : core.a1.tone(40),
            "onPrimary" : core.a1.tone(100),
            "primaryContainer" : core.a1.tone(90),
            "onPrimaryContainer" : core.a1.tone(10),
            "secondary" : core.a2.tone(40),
            "onSecondary" : core.a2.tone(100),
            "secondaryContainer" : core.a2.tone(90),
            "onSecondaryContainer" : core.a2.tone(10),
            "tertiary" : core.a3.tone(40),
            "onTertiary" : core.a3.tone(100),
            "tertiaryContainer" : core.a3.tone(90),
            "onTertiaryContainer" : core.a3.tone(10),
            "error" : core.error.tone(40),
            "onError" : core.error.tone(100),
            "errorContainer" : core.error.tone(90),
            "onErrorContainer" : core.error.tone(10),
            "background" : core.n1.tone(98),
            "onBackground" : core.n1.tone(10),
            "surface" : core.n1.tone(98),
            "surfaceBright" : core.n1.tone(98),
            "onSurface" : core.n1.tone(10),
            "surfaceContainer": core.n1.tone(94),
            "surfaceContainerLow": core.n1.tone(96),
            "surfaceContainerHigh": core.n1.tone(92),
            "surfaceContainerHighest": core.n1.tone(90),
            "surfaceVariant" : core.n2.tone(90),
            "onSurfaceVariant" : core.n2.tone(30),
            "outline" : core.n2.tone(50),
            "outlineVariant" : core.n2.tone(80),
            "shadow" : core.n1.tone(0),
            "inverseSurface" : core.n1.tone(20),
            "inverseOnSurface" : core.n1.tone(95),
            "inversePrimary" : core.a1.tone(80)
        })

    # /**
    #  * @param argb ARGB representation of a color.
    #  * @return Dark Material color scheme, based on the color's hue.
    #  */
    @staticmethod
    def dark(argb):
        core = CorePalette.of(argb);
        return Scheme({
            "primary" : core.a1.tone(80),
            "onPrimary" : core.a1.tone(20),
            "primaryContainer" : core.a1.tone(30),
            "onPrimaryContainer" : core.a1.tone(90),
            "secondary" : core.a2.tone(80),
            "onSecondary" : core.a2.tone(20),
            "secondaryContainer" : core.a2.tone(30),
            "onSecondaryContainer" : core.a2.tone(90),
            "tertiary" : core.a3.tone(80),
            "onTertiary" : core.a3.tone(20),
            "tertiaryContainer" : core.a3.tone(30),
            "onTertiaryContainer" : core.a3.tone(90),
            "error" : core.error.tone(80),
            "onError" : core.error.tone(20),
            "errorContainer" : core.error.tone(30),
            "onErrorContainer" : core.error.tone(80),
            "background" : core.n1.tone(6),
            "onBackground" : core.n1.tone(90),
            "surface" : core.n1.tone(6),
            "surfaceBright": core.n1.tone(24),
            "onSurface" : core.n1.tone(90),
            "surfaceContainer": core.n1.tone(12),
            "surfaceContainerLow": core.n1.tone(10),
            "surfaceContainerHigh": core.n1.tone(17),
            "surfaceContainerHighest": core.n1.tone(22),
            "surfaceVariant" : core.n2.tone(30),
            "onSurfaceVariant" : core.n2.tone(80),
            "outline" : core.n2.tone(60),
            "outlineVariant": core.n2.tone(30),
            "shadow" : core.n1.tone(0),
            "inverseSurface" : core.n1.tone(90),
            "inverseOnSurface" : core.n1.tone(20),
            "inversePrimary" : core.a1.tone(40)
        })

    def toJSON(self):
        return json.dumps(self.props)
