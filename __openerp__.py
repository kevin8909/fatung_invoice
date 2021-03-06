# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Autor:Kevin Kong (kfx2007@163.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	"name":"Fatung Tax",
	"author":"Kevin Kong",
	"description":"Customize Module For Fatung",
	"depends":["sale","account"],
	"data":[
		"fatung_data_view.xml",
		"fatung_tax_view.xml",
		"fatung_tax_out_view.xml"
	],
	"installable":True,
	"category":"Other",
}