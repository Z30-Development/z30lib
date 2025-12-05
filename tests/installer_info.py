from z30lib import installer

installer.download_app("Google Chrome")                       # Download an app (no installation)
installer.install_app("Visual Studio Code")                   # Install an app (no download specification)
installer.download_install_app("Git")                         # Install an app (with download specification)

# Downloads will appear in folder:
#        C:\Users\<USER>\Downloads
