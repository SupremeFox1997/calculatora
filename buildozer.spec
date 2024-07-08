[app]

# (str) Title of your application
title = MeatCalculator

# (str) Package name
package.name = meatcalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Permissions
# (full list here: https://developer.android.com/reference/android/Manifest.permission.html)
# e.g. android.permissions = INTERNET
android.permissions = INTERNET

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (str) Android API to use
android.api = 28

# (str) Minimum API required
android.minapi = 21

# (str) Android SDK directory path (if python-for-android was installed manually)
android.sdk_path = D:\AppData\platforms\android-35

# (str) Android NDK directory path (if python-for-android was installed manually)
android.ndk_path = D:\AppData\ndk\27.0.11902837

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok
android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Indicate whether the screen should stay on
android.wakelock = False

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Source files to exclude (let empty to include all the files)
source.exclude_exts = spec

# (list) List of Java .jar files to add to the classpath
# (e.g. jars = mylibrary.jar,mylibrary2.jar)
# jars = 

# (list) List of Java files to add to the classpath
# (e.g. srcfiles = mypackage/src/main/java)
# srcfiles = 

# (list) Logcat filters to use
# (e.g. logcat_filters = *:S python:D)
# logcat_filters = 
