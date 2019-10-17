FROM python:3.7-slim
WORKDIR /
COPY src src
COPY run.sh /
RUN chmod +x run.sh
ENTRYPOINT ["/run.sh"]
