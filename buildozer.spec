[app]
# (str) Title of your application
title = KPI Manager

# (str) Package name
package.name = kpimanager

# (str) Package domain (unique, 보통 reverse domain 형식)
package.domain = org.example.kpi

# (str) Source code directory
source.dir = .

# (str) Main .py file
source.main = main.py

# (list) Supported orientations
orientation = portrait

# (str) Application version
version = 0.1

# (list) Application requirements
# 여기서 필요한 라이브러리를 추가하세요 (예: sqlite3, requests)
requirements = python3,kivy,sqlite3,requests

# (str) Presplash screen (앱 시작 시 로딩 이미지)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Application icon
# icon.filename = %(source.dir)s/data/icon.png

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Features (e.g. for camera or GPS)
# android.features = android.hardware.camera, android.hardware.location

# (str) Entry point (일반적으로 main.py 그대로 둠)
entrypoint = main.py

# (str) Supported screens
# android.archs = arm64-v8a, armeabi-v7a, x86, x86_64

# (bool) Enable android logcat
log_level = 2

# (str) Custom package domain (optional)
# package.domain = org.yourdomain

# (str) Application category (e.g. Education, Productivity, Tools)
# android.category = Productivity

# (str) Min API Level (build.gradle 과 연결됨)
android.minapi = 21

# (str) Target API Level
android.api = 34

# (str) NDK API (for Cython 등)
android.ndk_api = 21

# (str) SDK version
android.sdk = 30.0.3

# (str) Build tools version
android.build_tools = 36.0.0

# (list) Extra Java jars to include
# android.add_jars = libs/some-lib.jar

# (list) Gradle dependencies (예: firebase, google play services)
# android.gradle_dependencies = com.google.firebase:firebase-analytics:17.2.2

# (str) Android log filters
# logcat_filters = *:S python:D

# (str) Android entry point (기본값 main.py)
# entrypoint = main.py

# (bool) Copy library instead of symlink
# copy_libs = 1


[buildozer]
# (str) Directory where buildozer will place files
build_dir = .buildozer

# (str) Log level (0 = quiet, 1 = normal, 2 = verbose, 3 = debug)
log_level = 2

# (bool) Use git (to update requirements if repo)
# use_git = 0

# (str) Path to SDK
android.sdk_path = /root/android-sdk

# (str) Path to NDK
android.ndk_path = /root/android-ndk

# (str) Path to Android cmdline-tools
android.cmdline_tools = /root/android-sdk/cmdline-tools/latest

# (str) Path to platform-tools (adb 등)
android.adb_path = /root/android-sdk/platform-tools/adb
