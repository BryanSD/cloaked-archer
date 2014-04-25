cloaked-archer
==============

Sample To-Do using distributed database backends

--------------

PostgreSQL Setup:

1) get prereqs 

    sudo apt-get install libreadline-dev flex bison git zlib1g-dev make build-essential

2) Get and compile postgres with BDR (bidirectional replication) support

    mkdir $HOME/bdr
    cd $HOME/bdr
    git clone -b bdr git://git.postgresql.org/git/2ndquadrant_bdr.git $HOME/bdr/postgres-bdr-src
    cd $HOME/bdr/postgres-bdr-src
    ./configure --prefix=$HOME/bdr/postgres-bdr-bin
    make install
    (cd contrib/btree_gist && make install)
    (cd contrib/bdr && make install)
    export PATH=$HOME/bdr/postgres-bdr-bin/bin:$PATH

3) Set up database storage location

    mkdir $HOME/data
    initdb -D $HOME/data

4) Configure postgres for BDR following https://wiki.postgresql.org/wiki/BDR_User_Guide#Configuration

5) Start postgresql and setup database

    postgres -D $HOME/data >logfile 2>&1 &
    createdb replicated_todo

5) Set up table for application

    psql replicated_todo
    CREATE TABLE todos (
        id varchar PRIMARY KEY,
        title varchar NOT NULL,
        description text NOT NULL
    );
    \q

6) Install python requirements

    pip install -r requirements.txt

7) Setup for stevedore

    python setup.py develop

8) Set up config and change values as needed

    cp sample.cfg app.cfg

8) Run as:

    python server.py postgresql
