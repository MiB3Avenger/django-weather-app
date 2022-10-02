# Django vite example

This is example app that combines Django and Vite + Vue.

Vue components are located in `frontend/js` folder. This app comes with Vue, Vuetify,
Vuex and Vue router included. Also on demo page we have 2 independent Vue apps along with
Django rendered elements.

In places where we have both Django and Vue app, any changes that are made to Vue app, will be
immediately visible since Vite supports hot module replacement (changes to js, vue and style files).

Another thing to note that in this example project we have used plain CSS along with Less and Sass
styling files as proof of concept (you should pick one for production and stick with it)

# Running the app


## Running with docker

Clone repository, switch dir to the cloned repo and run `compose up`
This will build Docker container and spin up Django application on `http://localhost:8000`
and vite dev server on port `http://localhost:3000/static/vite/`

Open browser and visit [http://localhost:8000](http://localhost:8000)


## Runing locally

You should be running Node v16.17.1 and Npm v8.15.0 or later for this to work.

Clone repository, switch dir to the cloned repo. Set up python virtualenv and activate it.
After you have activated virtualenv run following commands:
```
pip install -r requirements.txt
./manage migrate
npm install
```

If you want you can run single command, but you should have 2 terminals and start
Django server and Vite dev server separately.
Single command:
```
./manage.py runserver 0:8000 & npm run dev
```

If you have 2 terminals you can run:
```
./manage.py runserver 0:8000
```
and in second terminal
```
npm run dev
```

Open browser and visit [http://localhost:8000](http://localhost:8000)


# Building files for production

In production we don't want to run Vite dev server so we need to build frontend app.

To build your front end app run
```
npm run build
```

This will bundle your front-end app and save files in `./frontend/dist`. This folder is added
to the `STATICFILES_DIRS` in Django settings, and for Django to be able to access these files
you need to run `./manage.py collectstatic`.
