FROM ubuntu:bionic

RUN apt-get update \
  && apt-get install -y \
  bind9 \
  bind9utils \
  bind9-doc \
  tcpdump

# Enable IPv4
RUN sed -i 's/OPTIONS=.*/OPTIONS="-4 -u bind"/' /etc/default/bind9


# Expor a porta 53 (DNS)
EXPOSE 53/udp
EXPOSE 53/tcp


# Definir o comando para iniciar o BIND durante a inicialização
CMD ["named", "-g", "-u", "bind"]

# Comando para manter o contêiner rodando em loop
# CMD ["tail", "-f", "/dev/null"]
