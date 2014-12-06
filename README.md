Fig Demo
========

Demo projects using [Fig][1] as development environments for Python.


flask-mongodb
-------------

### 1. Build `mongodb` image

    $ git clone https://github.com/RussellLuo/dockerfiles.git
    $ cd dockerfiles/ubuntu/mongodb
    $ sudo docker build -t mongodb:dev .

See [Dockerfiles][2] for more details.

### 2. Run the web app

    $ git clone https://github.com/RussellLuo/fig-demo.git
    $ cd flask-mongodb
    $ sudo fig up

### 3. Access the web app

    $ curl http://localhost:5000


[1]: https://github.com/docker/fig
[2]: https://github.com/RussellLuo/dockerfiles
