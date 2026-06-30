[app]
title = 刷题助手
package.name = quizapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.1.0
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.gradle_dependencies = 
android.arch = armeabi-v7a
# 新增下面两行（必须）
android.accept_sdk_license = True
android.build_tools_version = 33.0.3
p4a.branch = master
[buildozer]
log_level = 2
warn_on_root = 1
