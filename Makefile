CXX = skm clang++
CXXFLAGS = -Wall

TARGET = build/main.exe

SOURCES = $(wildcard src/*.cpp) \
          $(wildcard include/*.cpp)

all: $(TARGET)

$(TARGET): $(SOURCES)
	mkdir -p build
	$(CXX) $(SOURCES) -o $(TARGET) $(CXXFLAGS)

clean:
	rm -f $(TARGET)
