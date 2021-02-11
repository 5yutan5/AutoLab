from enum import Enum

import AutoLab.utils.resources_icon
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStyle, qApp

# ICON_FOLDER_PATH = "AutoLab/images/"


class IconName(Enum):
    ADD_BEHAVIOR = ":AddBehavior_16x.png"
    ADD_CONNECTION = ":AddConnection_16x.png"
    CHECK_MARK = ":Checkmark_16x.png"
    COLLAPSE_LEFT = ":CollapseLeft_lg_16x.png"
    COLLAPSE_UP = ":CollapseUp_lg_16x.png"
    CONNECT = ":Connect_16x.png"
    CONNECT_PLUGGED = ":ConnectPlugged_16x.png"
    CONNECT_UNPLUGGED = ":ConnectUnplugged_16x.png"
    CONTINUE = ":DebugContinue_16x.png"
    DISCONNECT = ":Disconnect_16x.png"
    DYNAMIC = ":Dynamic_16x.png"
    DYNAMIC_GROUP = ":DynamicGroup_16x.png"
    EXPAND_ARROW = ":ExpandArrow_16x.png"
    EXPAND_DOWN = ":ExpandDown_lg_16x.png"
    EXPAND_RIGHT = ":ExpandRight_lg_16x.png"
    FOLDER_OPENED = ":FolderOpened_16x.png"
    LOADING = ":Loading_16x.png"
    OPEN_FOLDER = ":OpenFolder_16x.png"
    RUN = ":run_16x.png"
    STATUS_RUN = ":StatusRun_16x.png"
    STOP = ":Stop_16x.png"
    STOP_STAGE = ":Stop_white_48x.png"


def icon(name: IconName) -> QIcon:
    return QIcon(name.value)


def default_icon(icon: QStyle.StandardPixmap) -> QIcon:
    return qApp.style().standardIcon(icon)
