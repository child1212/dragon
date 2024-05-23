#!/usr/bin/python
#coding=utf-8

import os
import sys
import inspect


# 检测脚本所在的路径
def script_path():
    this_file = inspect.getfile(inspect.currentframe())
    path = os.path.abspath(os.path.dirname(this_file))
    return path


def user_id():
    platform = sys.platform
    if platform == 'win32':
        return os.environ["USERNAME"]
    else:
        return os.getuid()


g_role_id               = user_id()

g_programmer_mode       = True

# 项目的顶层路径设计
g_cur_dir               = script_path()
g_prj_home              = os.path.normpath(os.path.join(g_cur_dir, "../"))
g_client_home           = os.path.normpath(os.path.join(g_prj_home, "client"))
g_external_home         = os.path.normpath(os.path.join(g_cur_dir, "../external"))
g_script_home           = os.path.normpath(os.path.join(g_client_home, "Assets/HomeLand/LuaScript"))
g_assets_home              = os.path.normpath(os.path.join(g_client_home, "Assets/"))
g_art_home              = os.path.normpath(os.path.join(g_client_home, "Assets/HomeLand/"))

print("----------------------[%s's cfg]--------------------" % g_role_id)
print("[cur_dir ]:" + g_cur_dir)
print("[prj_home]:" + g_prj_home)
print("[prj_external_home]:" + g_external_home)
print("[script_home]:" + g_script_home)
print("[art_home]:" + g_art_home)
print("----------------------------------------------------------")
