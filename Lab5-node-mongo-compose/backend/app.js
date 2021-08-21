const express = require('express')
const restfull = require('node-restful')
const mongoose = require('mongoose');
const bodyParser = require('body-parser')
const cors = require('cors');
const restful = require('node-restful')
const server = express()
//Set up default mongoose connection
mongoose.Promise = global.Promise
const mongoDB = 'mongodb://db/mydb';
mongoose.connect(mongoDB, {useMongoClient: true, useNewUrlParser: true })
//Get the default connection
var db = mongoose.connection;
//Bind connection to error event (to get notification of connection errors)
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

// endpoint
server.get('/',(req, res, next) => res.send('Backend'))


// Middlewares
server.use(bodyParser.urlencoded({extended:true}))
server.use(bodyParser.json())
server.use(cors())

// ODM
const Client = restful.model('Client', {
    name: { type: String, required: true }
})

// Rest API
Client.methods(['get', 'post', 'put', 'delete'])
Client.updateOptions({new: true, runValidators: true})

// Routes
Client.register(server, '/clients')

// start server
server.listen(3000)