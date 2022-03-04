const path = require('path')
const fileURLToPath = require('url').fileURLToPath


const express = require('express');
const expressWs = require('express-ws')(express());
const http = require('http');

// Our port
let port = 6789;

// App and server
let app = express();
let server = http.createServer(app).listen(port);    

// Apply expressWs
expressWs(app, server);

app.set('views', path.join(__dirname, 'views'));

// Get the route / 
app.get('/', (req, res) => {
    res.status(200).send("Welcome to our app");
});

// Get the /ws websocket route
app.ws('/ws', async function(ws, req) {
    ws.on('message', async function(msg) {
        // What was the message?
        console.log(msg);
        // Send back some data
        ws.send(JSON.stringify({
            "append" : true,
            "returnText" : "I am using websockets!"
        }));
    });
});