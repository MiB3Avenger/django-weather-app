# Django Weather App

This is weather app that combines Django with API endpoints and Vite + Vue with TailwindCSS.

Vue components are located in `frontend/js` folder. This app comes with Vue, TailwindCSS,
Vuex and Vue router included.

In places where we have both Django and Vue app, any changes that are made to Vue app, will be
immediately visible since Vite supports hot module replacement (changes to js, vue and style files).

Thanks to [@elrik](https://gitlab.com/elrik/django-vite-example) for initial boilerplate for Django + Vite.


# Contents
- [Running the app](#running-the-app)
    - [Running with Docker](#running-with-docker)
    - [Running Locally](#running-locally)
- [Building Files for Production](#building-files-for-production)
- [Customizing Repository](#customizing-repository)


<a id="running-the-app"></a>

# Running the app


<a id="running-with-docker"></a>

## Running with docker

Clone repository, switch dir to the cloned repo and run `compose up`
This will build Docker container and spin up Django application on `http://localhost:8000`
and vite dev server on port `http://localhost:3000/static/vite/`

Open browser and visit [http://localhost:8000](http://localhost:8000)


<a id="running-locally"></a>

## Running locally

You should be running Node v16.17.1 and Npm v8.15.0 or later for this to work.

Clone repository, switch dir to the cloned repo. Set up python virtualenv and activate it.
After you have activated virtualenv run following commands:
```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
npm install
npm ci
```

If you want you can run single command, but you should have 2 terminals and start
Django server and Vite dev server separately.
Single command:
```sh
./manage.py runserver 0:8000 & npm run dev
```

If you have 2 terminals you can run:
```sh
./manage.py runserver 0:8000
```
and in second terminal   
```sh
npm run dev
```

Open browser and visit [http://localhost:8000](http://localhost:8000)


<a id="building-files-for-production"></a>

# Building files for production

In production we don't want to run Vite dev server so we need to build frontend app.

To build your front end app run
```sh
npm install
npm ci
npm run build
```

This will bundle your front-end app and save files in `./frontend/dist`. This folder is added to the `STATICFILES_DIRS` in Django settings, and for Django to be able to access these files you need to run `./manage.py collectstatic`.


<a id="customizing-repository"></a>

# Customizing Repository

While making changes to the project, you may want to keep few things in mind. When wanting to change `my_project` folder to of your choice, you'll have to update the following files with your project folder name.

1. tailwind.config.js
2. manage.py
3. my_project/asgi.py
4. my_project/wsgi.py

And finally, update `APP_NAME` in `my_project/settings/base.py` to your folder name. This will allow django to recognize project apps easily. If you encounter any issues, please create an issue and I'll do my best to fix your problem.