Exercício 1
```sh
curl localhost:3000  or  curl -X GET localhost:3000
```
```sh
curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{ "foo": "bar" }' \
    localhost:3000
```
```sh
curl --request POST \
    --header 'Content-Type: application/json' \
    --header 'Authorization: ApiKey EXAMPLE-TOKEN' \
    --data '{ "foo": "bar" }' \
    localhost:3000
```

Exercício 2
```sh
curl google.com
```
```sh
curl -L google.com
```

Exercício 3
```sh
wget betrybe.com
```

Exercício 5
```sh
telnet 127.0.0.1 8085
```




Exercício 6
```sh
curl localhost:8085
```
```sh
curl --request POST \
    --data "{ \"foo\": \"bar\" }" \
    --header 'Content-Type: application/json' \
    --header 'Foo-Bar-Header: foo-bar' \
    localhost:8085/foo-bar
```

Exercício 8
```sh
nc -u 127.0.0.1 8084
```

Exercício 9
```sh
curl localhost:8084
```

Exercício 10
```sh
 mkdir diretorio && cd diretorio
 python3 -m http.server 80
```
```sh
sudo tar xvzf ./ngrok-v3-stable-linux-amd64.tgz
```
```sh
 ./ngrok http 80
```

