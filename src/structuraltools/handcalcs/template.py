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
import json
from typing import Any, NamedTuple

import attrs
from pint import Quantity

from structuraltools.units import Numeric


resources = importlib.resources.files("structuraltools.handcalcs.resources")
with open(resources.joinpath("template.json")) as file:
    _templates = json.load(file)


class Result[T](NamedTuple):
    str: str
    val: T

class ArgFormat(NamedTuple):
    type: type
    format: str

arg_settings: dict[str, ArgFormat] = {
    "Quantity": ArgFormat(Quantity, "~L.4g"),
    "float": ArgFormat(float, ".4g"),
    "int": ArgFormat(int, ".4g")
}

def format_arg(arg: Any, arg_settings: dict[str, ArgFormat]) -> str:
    for arg_format in arg_settings.values():
        if isinstance(arg, arg_format.type):
            return format(arg, arg_format.format)
    else:
        return format(arg)

@attrs.define()
class EqSettings:
    return_str: bool
    eq_layout: str
    ref_layout: str
    arg_settings: dict[str, ArgFormat] = arg_settings

@attrs.define()
class EqTemplate:
    org: str
    code: str
    id: str
    result_sym: str
    arg_syms: list[str]
    expr: str
    layout: str

    def process[T](self, settings: EqSettings, result: T, *args: Any) -> Result[T]:
        if settings.return_str:
            arg_strs = [format_arg(arg, settings.arg_settings) for arg in args]
            ref_layout = _templates["refs"][settings.ref_layout]
            if settings.eq_layout:
                eq_layout = _templates["eqs"][settings.eq_layout]
            else:
                eq_layout = _templates["eqs"][self.layout]
            eq_str = eq_layout.format(
                self.result_sym,
                self.expr.format(*self.arg_syms),
                self.expr.format(*arg_strs),
                format_arg(result, settings.arg_settings),
                ref_layout.format(self.org, self.code, self.id))
        else:
            eq_str = ""
        return Result(eq_str, result)
        




