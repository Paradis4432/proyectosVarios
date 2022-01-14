const express = require('express');
const router = express.Router();
const path = require('path');
const session = require('express-session');
const app = express();
const bodyParser = require('body-parser');
const methodOverride = require('method-override');
//const cors = require('cors');

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(methodOverride('_method'));
app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));

//const corsOptions = {
//    origin: "*",
//};

//app.use(cors(corsOptions));

app.listen(3000, () => { console.log('Server started at port 3000'); });

app.get('/', (req, res) => {
    //render home.ejs and send the number 2 as a parameter called num
    
    res.render('home', {fileName: "i0.jpg", test: "something", test2: ["a", "b", "c", "d"]});
});

app.post("/upload/image", (req, res) => {
    console.log("this is a test")
    res.send("uploaded")
})