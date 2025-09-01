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


import json

import pytest

from structuraltools.core import template


with open("tests/structuraltools/core/resources/test_display.json") as file:
    templates = json.load(file)


def test_format_arg():
    assert False

class TestEqTemplate:
    def setup_method(self, method):
        self.eq_template = template.EqTemplate(**templates["eqs"]["test_equation_template"])
        self.result = -1
        self.args = [0, 1, 2, 3, 4, 5, 6]

    def test_process(self):
        settings = template.EqSettings(
            return_str=True,
            eq_layout=None,
            ref_layout="short")
        result = self.EqTemplate.process(settings, self.result, *self.args)
        assert False
