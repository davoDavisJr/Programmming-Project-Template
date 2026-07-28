CXX ?= clang++
CXXFLAGS ?= -std=c++20 -Wall -Wextra -Wpedantic -g
TARGET ?= build/main

SOURCES := $(wildcard src/*.cpp)
HEADERS := $(wildcard include/*.h) $(wildcard include/*.hpp)

.PHONY: all run clean

all: $(TARGET)

$(TARGET): $(SOURCES) $(HEADERS)
	mkdir -p build
	$(CXX) $(CXXFLAGS) $(SOURCES) -I include -o $(TARGET)

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f $(TARGET) $(TARGET).exe build/*.o
