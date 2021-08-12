mkdir static
cd static
mkdir css
mkdir js
mkdir images
mkdir favicon
cd ..
touch css/main.css
touch js/main.js
mkdir templates
touch templates/main.html
touch templates/template.html.example
cp ~/Documents/fwa_template/main.html.example templates/main.html
cp ~/Documents/fwa_template/template.html.example templates/template.html.example
touch app.py
touch config.py.example
if ["$1" = "-d"]; then
  cp ~/Documents/fwa_template/app-d.py app.py
  cp ~/Documents/fwa_template/config-d.py.example config.py.example
  touch db.py
  if ["$2" = "pg"]; then
    cp ~/Documents/fwa_template/db-pg.py db.py
    cp ~/Documents/fwa_template/requirements-d-pg.txt requirements.txt
  else
    cp ~/Documents/fwa_template/db-mysql.py db.py
    cp ~/Documents/fwa_template/requirements-d-mysql.txt requirements.txt
  fi
else
  cp ~/Documents/fwa_template/config.py.example config.py.example
  cp ~/Documents/fwa_template/app.py app.py
  cp ~/Documents/fwa_template/requirements.txt requirements.txt
fi
