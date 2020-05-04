LEAP_LIBRARY := ./lib/libLeap.so -Wl,-rpath,../lib/x64

Sample: Sample.cpp
	$(CXX) -Wall -g -I../include Sample.cpp -o Sample $(LEAP_LIBRARY)

clean:
	rm -rf Sample Sample.dSYM
