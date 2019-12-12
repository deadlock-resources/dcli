CC=gcc
CXXFLAGS=-std=standard -Wall -Werror -Wextra -pedantic

VPATH=./app/:./template/:./success/
SRC=$(wildcard *.c)
OBJ=$(SRC:.c=.o)
BIN=app

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) -o $(BIN) $(OBJ)

$(OBJ): $(SRC)
	$(CC) -c $(SRC) -I $(VPATH)

clean:
	rm -f *.o
	rm -f $(BIN)