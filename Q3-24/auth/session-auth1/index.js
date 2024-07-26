const express = require('express');
const sessions = require('express-session');

const app = express();

app.use(
  sessions({
    secret: 'some secret',
    cookie: {
      maxAge: 1000 * 60 * 60 * 24, // 24 hours
    },
    resave: true,
    saveUninitialized: false,
  })
);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// @todo register routes

app.listen(3000, () => {
  console.log(`Server Running at port 3000`);
});


const HomeHandler = require('./handlers/home.js');

app.get('/', HomeHandler);


const LoginHandler = require('./handlers/login.js');

app.get('/login', LoginHandler);

const ProcessLoginHandler = require('./handlers/process-login.js');

app.post('/process-login', ProcessLoginHandler);

const LogoutHandler = require('./handlers/logout.js');

app.get('/logout', LogoutHandler);