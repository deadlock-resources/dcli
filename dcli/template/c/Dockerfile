FROM gcc:9.2.0
WORKDIR /usr/src/app
COPY src/* ./
COPY run.sh ./
RUN chmod +x run.sh
ENTRYPOINT ["./run.sh"]
