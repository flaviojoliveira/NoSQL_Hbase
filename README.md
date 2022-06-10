# Etapas para criar o container
- Fazer o pull da imagem
```
docker pull dajobe/hbase
```

- Checar se o pull da imagem ocorreu corretamente
```
docker images
```

- Criar diretório de dados
```
mkdir data
```

- Executar o container usando a imagem
```
id=$(docker run --name=hbase-docker -h hbase-docker -d -v $PWD/data:/data dajobe/hbase)
```

- Conferir se o container está rodando ou não
```
docker ps
```

- Entrar no container
```
docker exec -it hbase-docker bash
```

- Pegar o IP do arquivo host
```
cat /etc/hosts
```

- Atualizar o IP pelos arquivos locais do sistema

- Checar o status do HBase no browser

- Abrir o Shell do HBase e executar comandos
```
docker run --rm -it --link $id:hbase-docker dajobe/hbase hbase Shell
```
