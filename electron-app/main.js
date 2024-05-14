const { app, BrowserWindow } = require('electron');
const path = require('path');
const { exec } = require('child_process');

let mainWindow;
let backendProcess;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: true
        }
    });

    // Load the React app
    mainWindow.loadURL('http://localhost:3000');

    mainWindow.on('closed', function () {
        mainWindow = null;
    });
}

app.on('ready', () => {
    // Start the Flask backend
    backendProcess = exec('pipenv run python server.py', { cwd: path.join(__dirname, 'server') });

    backendProcess.stdout.on('data', (data) => {
        console.log(`Backend: ${data}`);
    });

    backendProcess.stderr.on('data', (data) => {
        console.error(`Backend error: ${data}`);
    });

    backendProcess.on('close', (code) => {
        console.log(`Backend process exited with code ${code}`);
    });

    // Start the React frontend
    const frontendProcess = exec('npm start', { cwd: path.join(__dirname, 'client') });

    frontendProcess.stdout.on('data', (data) => {
        console.log(`Frontend: ${data}`);
    });

    frontendProcess.stderr.on('data', (data) => {
        console.error(`Frontend error: ${data}`);
    });

    frontendProcess.on('close', (code) => {
        console.log(`Frontend process exited with code ${code}`);
    });

    createWindow();
});

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', function () {
    if (mainWindow === null) {
        createWindow();
    }
});

app.on('will-quit', () => {
    // Ensure the backend process is terminated when Electron quits
    if (backendProcess) {
        backendProcess.kill();
    }
});
