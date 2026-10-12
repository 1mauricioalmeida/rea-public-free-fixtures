const { app, BrowserWindow } = require('electron');
app.whenReady().then(() => new BrowserWindow({webPreferences:{nodeIntegration:false,contextIsolation:true}}));
