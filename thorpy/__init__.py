__version__ = "1.5.2a"

import sys
import os

# verify that pygame is on the machine
try:
    import pygame
except Exception:
    print("Pygame doesn't seem to be installed on this machine.")


# add thorpy folder to Windows and Python search paths
THORPY_PATH = os.path.abspath(os.path.dirname(__file__))
##THORPY_PATH = "./" #for py2exe
try:
    os.environ['PATH'] = ';'.join((THORPY_PATH, os.environ['PATH']))
    sys.path.append(THORPY_PATH)
except Exception:
    print("Couldn't add Thor to sys.path...\nThorPy path : " + THORPY_PATH)

USEREVENT = pygame.USEREVENT + 1 #horpy takes one event on pygame's userevents
THORPY_EVENT = pygame.USEREVENT

#import subpackages
import thorpy.elements
import thorpy.menus
import thorpy._utils
import thorpy.miscgui
import thorpy.painting as painting
import thorpy.miscgui.application as application
import thorpy.miscgui.storage as storage
import thorpy.painting.graphics as graphics

##import testmodule

from thorpy._utils.images import load_image, change_color_on_img, change_color_on_img_ip

from thorpy.elements.launchers.browserlauncher import BrowserLauncher
from thorpy.elements.launchers.dropdownlistlauncher import DropDownListLauncher
from thorpy.elements.launchers.paramsetterlauncher import ParamSetterLauncher
from thorpy.elements.launchers.colorsetterlauncher import ColorSetterLauncher
from thorpy.elements.paramsetter import ParamSetter
from thorpy.elements.background import Background
from thorpy.elements.image import Image
from thorpy.elements.box import Box, BarBox
from thorpy.elements.browserlight import BrowserLight
from thorpy.elements.browser import Browser
from thorpy.elements.checker import Checker
from thorpy.elements.clickable import Clickable
from thorpy.elements._wrappers import make_button, make_text, make_alert, make_image_button
from thorpy.elements._wrappers import launch_alert, launch_blocking_alert
from thorpy.elements._wrappers import launch_choices, launch_blocking_choices
from thorpy.elements._wrappers import make_alert
from thorpy.elements._wrappers import make_stored_ghost as make_group
from thorpy.elements._wrappers import make_font_setter, make_fontsize_setter
from thorpy.elements._wrappers import make_font_options_setter, make_display_options_setter, make_global_display_options
from thorpy.elements.colorsetter import ColorSetter
from thorpy.elements.ddlf import DropDownListFast as DropDownList
from thorpy.elements.draggable import Draggable, ClickDraggable
from thorpy.elements.element import Element
from thorpy.elements.ghost import Ghost
from thorpy.elements.hoverable import Hoverable
from thorpy.elements.hoverzone import HoverZone
from thorpy.elements.inserter import Inserter
from thorpy.elements.keypressable import KeyPressable
from thorpy.elements.keytogglable import KeyTogglable
from thorpy.elements.paramsetter import ParamSetter
from thorpy.elements.pressable import Pressable
##from thorpy.elements.text import MultilineText
from thorpy.elements.text import OneLineText, MultilineText
from thorpy.elements.slidersetter import SliderXSetter as SliderX
from thorpy.elements.togglable import Togglable
from thorpy.elements.line import Line
from thorpy.elements._makeuputils._halo import Halo
from thorpy.elements._makeuputils._shadow import StaticShadow
from thorpy.elements._makeuputils._shadow import DynamicShadow

# menus:
from thorpy.menus.tickedmenu import TickedMenu as Menu
from thorpy.menus.basicmenu import BasicMenu

# miscellaneous stuff, constants, parameters
from thorpy.miscgui.application import Application
from thorpy.miscgui.reaction import Reaction, ConstantReaction
from thorpy.miscgui import constants, functions
from thorpy.miscgui.functions import get_screen
from thorpy.miscgui.functions import get_current_application as get_application
from thorpy.miscgui.functions import get_current_menu
from thorpy.miscgui import style
from thorpy.miscgui import painterstyle
from thorpy.miscgui import parameters
from thorpy.miscgui.initializer import Initializer
from thorpy.miscgui.state import State
from thorpy.miscgui.storage import Storer, store
from thorpy.miscgui.title import Title
from thorpy.miscgui.varset import VarSet
from thorpy.miscgui import theme
from thorpy.miscgui.theme import set_theme as set_theme
from thorpy.miscgui.metadata import MetaDataManager
from thorpy.miscgui.pools import TogglablePool, RadioPool

from thorpy.miscgui.launchers.launcher import set_launcher, make_launcher, get_launcher, Launcher, make_ok_cancel_box, launch, make_ok_box

from thorpy.painting.writer import Writer
from thorpy.painting import painters
from thorpy.painting import makeup
##from thorpy.painting.painters.imageframe import ButtonImage
from thorpy.painting import mousecursor

from thorpy.gamestools import basegrid
from thorpy.gamestools.basegrid import BaseGrid
from thorpy.gamestools.grid import Grid, PygameGrid

del thorpy, pygame, os, sys
