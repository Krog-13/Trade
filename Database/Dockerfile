FROM postgres:14.3
ENV POSTGRES_PASSWORD=spoon
ENV POSTGRES_USER=spoon
ENV POSTGRES_DB=darwin
COPY create_fixture.sql /docker-entrypoint-initdb.d/create_fixtures.sql