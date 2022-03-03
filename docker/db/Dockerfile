FROM postgres:12

LABEL description="Postgresql shopping database"

ENV LANG en_US.utf8

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias ${LANG}

RUN mkdir -p /logs && chown postgres:postgres -R /logs

