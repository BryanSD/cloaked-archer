cloaked-archer
==============

Sample To-Do using distributed database backends

PostgreSQL Setup:

1) sudo apt-get install postgresql postgresql-server-dev-9.1
2) sudo -u postgres psql postgres
3) Change the postgres role's password (\q to quit the prompt)

    \password postgres

4) (Optional) Create role for app with login and create privs

    create role todo_admin with login password 'password' createdb

5) Set up table (run psql as desired role)

    createdb tododb
    psql -U user tododb
    CREATE TABLE todos (
        id SERIAL,
        title varchar NOT NULL,
        description text NOT NULL,
        PRIMARY KEY (id)
    );

6) pip install -r requirements.txt

7) python setup.py develop

8) Run as:

    python server.py postgresql tododb user password
