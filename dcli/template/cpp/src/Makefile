CC=g++
CXXFLAGS=-std=c++17 -Wall -Werror -Wextra -pedantic

VPATH=./app/:./template/:./success/
SRC=$(wildcard *.cpp)
OBJ=$(SRC:.cpp=.o)
BIN=app

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) -o $(BIN) $(OBJ)

$(OBJ): $(SRC)
	$(CC) -c $(SRC) -I $(VPATH)

clean:
	rm -f *.o
	rm -f $(BIN)
