require('dotenv').config()

const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

app.set('view engine', "ejs")

app.get('', (req, res) => {
    res.render('base')
});


const exampleRouter = require('./routes/example')
const userRouter = require('./routes/users')

app.use('/example', exampleRouter)
app.use('/users', userRouter)
app.use(express.static("public"));
 

//This sets the open port to value of const PORT
app.listen(PORT, ()=> {
    console.log(`App listening on port ${PORT}`)
});

app.use((req, res, next) => {
    res.status(404).send("<h1>Error 404</h1>Sorry can't find that!")
});