const express = require('express');
// la base del backend, nosotros vemos node con express. 

const router = express.Router();
// router se usa mayormente para post y delete, pero tambien se puede usar para get y post, leer documentacion porque router es grande y basico. 

const path = require('path');
//en este caso usamos path para tener el path.join

const session = require('express-session');
const app = express();
//app es la estructura del backend, por ejemplo app.get("/", ....), sin app uno no podria definir la ruta del / tan facil. 

const bodyParser = require('body-parser');
//elimina ciertos errores a la hora de hacer requests

const methodOverride = require('method-override');
// usado para reescribi el _method en el app, tambien elimina un par de errores, un detalle util

//const cors = require('cors');
// hay un error insufrible, "Cross-Origin request bloqued .." cors soluciona esto pero es recomendable mirar tutoriales y leer la documentacion. 
// https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors

app.set('views', path.join(__dirname, 'views'));
// definimos la ubicacion de las vistas en __dirname* /views
// *__dirname es la ubicacion de la carpeta actual

app.set('view engine', 'ejs');
// y definimos que queremos ejs como motor para renderizar las vistas 

app.use(express.static("public"));
// tambien podemos usar la carpeta directamente entonces cuando queremos importar un css podemos usar href="css/name.css", util cuando queremos ir cambiando de carpeta, sino tambien se puede
// definir la carpeta public/css e importarlo directamente. 

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
// permite utilizar archivos json, por ahora no hace falta que te enfoques en esto 

app.use(methodOverride('_method'));

app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));
//esto agrega una serie de detalles que no son relativos para el momento. 

//const corsOptions = {
//    origin: "*",
//};

//app.use(cors(corsOptions));

app.listen(3000, () => { console.log('Server started at port 3000'); });
// escuchamos en el puerto 3000, y enviamos a la consola del backend un mensaje para saber que todo esta bien


app.get('/', (req, res) => {
    //render home.ejs and send the number 2 as a parameter called num
    res.render("home");
});
// podemos usar app.[get/post/all] para manejar los distintos requests, es recomendable leer la documentacion sobre esto ya que es complicado entender cada detalle
// https://expressjs.com/en/guide/routing.html