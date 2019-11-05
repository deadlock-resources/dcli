# java version, may be change
FROM openjdk:8-jdk-slim
WORKDIR /
COPY src src
COPY run.sh /
RUN chmod +x run.sh
ENTRYPOINT ["/run.sh"]