# Copyright (C) 2025 Joe Bears
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import importlib.resources
from typing import Annotated, Union

from numpy import ndarray
import pint


resources = importlib.resources.files("structuraltools.units.resources")

unit = pint.UnitRegistry(resources.joinpath("units"))
unit.formatter.default_format = "~"


type Numeric = Union[int, float, Annotated[pint.Quantity, float]]
type NumericArray = Union[ndarray, Annotated[pint.Quantity, ndarray]]

type Area = Annotated[pint.Quantity, float, "[length]**2]"]
type Force = Annotated[pint.Quantity, float, "[force]"]
type Length = Annotated[pint.Quantity, float, "[length]"]
type LineLoad = Annotated[pint.Quantity, float, "[force]/[length]"]
type Moment = Annotated[pint.Quantity, float, "[moment]"]
type MomentOfInertia = Annotated[pint.Quantity, float, "[length]**4"]
type Pressure = Annotated[pint.Quantity, float, "[pressure]"]
type SectionModulus = Annotated[pint.Quantity, float, "[length]**3"]
type Stress = Annotated[pint.Quantity, float, "[pressure]"]
type TorsionalConstant = Annotated[pint.Quantity, float, "[length]**4"]
type UnitWeight = Annotated[pint.Quantity, float, "[unit_weight]"]
type Velocity = Annotated[pint.Quantity, float, "[velocity]"]
type WarpingConstant = Annotated[pint.Quantity, float, "[length]**6"]


__all__ = [
    "Area",
    "Force",
    "Length",
    "LineLoad",
    "Moment",
    "MomentOfInertia",
    "Numeric",
    "NumericArray",
    "Pressure",
    "SectionModulus",
    "Stress",
    "TorsionalConstant",
    "unit",
    "UnitWeight",
    "Velocity",
    "WarpingConstant"
]
