Hybrid App Starter
================

Designed as a starter app for cross platform hybrid apps. 

-----
## Dependencies
Development on windows

Java JDK 

Android SDK 

Node

Global Electron
```
npm install -g electron
```
Global Cordova
```
npm install -g cordova
```
To check for cordova requirements navigate to cordova build directory and execute:
```
cordova requirements
```

-----
## Download/Include
First Download/Clone the repo or get it from npm/bower with
```
 npm install -
 bower install -
```

-----
## Building the Application
to build the web app into an electron wrapper enter the command
```
gulp build-electron
```
to build the web app into a cordova wrapper enter the command
```
gulp build-cordova
```
to build everything
```
gulp build-all
```

-----
## Running App
Running in chrome
```
npm run web
```
Running in cordova emulator
```
npm run cordova
```
Running on mobile device
```
npm run cordova-device
```
Running App on desktop
```
npm run electron
```

-----
## Packaging Application
package the cordova movile app
```
gulp package-cordova
```
package the electron desktop app
```
gulp package-electron
```
package web app
```
gulp package-web
```
package all apps
```
gulp package-all
```