'''
    Copyright (C) 2013  Povilas Kanapickas <povilas@radix.lt>
    Copyright (C) 2018  Monika Kairaityte <monika@kibit.lt>

    This file is part of cppreference-doc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see http://www.gnu.org/licenses/.
'''

from index_transform.common import IndexTransform
from xml_utils import xml_escape

class Index2Devhelp(IndexTransform):

    def __init__(self, out_file):
        super().__init__()
        self.out_file = out_file

    def get_mark(self, el):
        if el.tag == 'const': return 'macro'
        elif el.tag == 'function': return 'function'
        elif el.tag == 'constructor': return 'function'
        elif el.tag == 'destructor': return 'function'
        elif el.tag == 'class': return 'class'
        elif el.tag == 'enum': return 'enum'
        elif el.tag == 'typedef': return 'typedef'
        elif el.tag == 'specialization': return 'class'
        elif el.tag == 'overload': return 'function'
        # devhelp does not support variables in its format
        elif el.tag == 'variable': return ''
        return ''

    def process_item_hook(self, el, full_name, full_link):
        self.out_file.write('<keyword type="' + xml_escape(self.get_mark(el))
                    + '" name="' + xml_escape(full_name)
                    + '" link="' + xml_escape(full_link) + '"/>\n')
        IndexTransform.process_item_hook(self, el, full_name, full_link)

