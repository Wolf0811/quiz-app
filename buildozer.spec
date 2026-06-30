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
# (可选) 如果需要 64 位 APK，取消下一行注释
# android.arch = arm64-v8a
p4a.branch = master
p4a.source_dir = 
p4a.bootstrap = sdl2
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_version = 9.0
ios.ios_deploy_target = 9.0
[buildozer]
log_level = 2
warn_on_root = 1
