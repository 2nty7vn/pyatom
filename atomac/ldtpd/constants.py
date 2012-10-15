# Copyright (c) 2012 VMware, Inc. All Rights Reserved.

# This file is part of ATOMac.

#@author: Nagappan Alagappan <nagappan@gmail.com>
#@copyright: Copyright (c) 2009-12 Nagappan Alagappan
#http://ldtp.freedesktop.org

# ATOMac is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 and no later version.

# ATOMac is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License version 2
# for more details.

# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301 USA.
"""Constants class."""

abbreviated_roles = {
    "AXWindow" : "frm",
    "AXTextArea" : "txt",
    "AXTextField" : "txt",
    "AXButton" : "btn",
    "AXStaticText" : "lbl",
    "AXRadioButton" : "rbtn",
    "AXSlider" : "sldr",
    "AXCell" : "tblc",
    "AXImage" : "img",
    "AXToolbar" : "tbar",
    "AXScrollBar" : "scbr",
    "AXMenuItem" : "mnu",
    "AXCheckBox" : "chk",
    "AXTabGroup" : "ptl",
    "AXList" : "lst",
    # Not sure what"s the following object equivalent in LDTP
    "AXMenuButton" : "cbo", # Maybe combo-box ?
    "AXRow" : "tblc",
    #"AXColumn" : "tblc",
    "AXTable" : "tbl",
    "AXScrollArea" : "sar",
    "AXOutline" : "otl",
    "AXValueIndicator" : "val",
    "AXDisclosureTriangle" : "dct",
    "AXGroup" : "grp",
    }
ldtp_class_type = {
    "AXWindow" : "frame",
    "AXTextArea" : "text",
    "AXTextField" : "text",
    "AXButton" : "push_button",
    "AXStaticText" : "label",
    "AXRadioButton" : "radion_button",
    "AXSlider" : "slider",
    "AXCell" : "table_cell",
    "AXImage" : "image",
    "AXToolbar" : "toolbar",
    "AXScrollBar" : "scroll_bar",
    "AXMenuItem" : "menu_item",
    "AXCheckBox" : "check_box",
    "AXTabGroup" : "page_tab_list",
    "AXList" : "list",
    "AXRow" : "table_cell",
    "AXTable" : "table",
    "AXScrollArea" : "scroll_area",
    }
