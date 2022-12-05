#good example of inheritance

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC): #Stream is an abstract class

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened: 
            raise InvalidOperationError("Stream is alredy opened.")
        self.opened = True

    def close(self):
        if not self.opened: 
            raise InvalidOperationError("Stream is alredy closed.")
        self.opened = False

    @abstractmethod
    def read(self): #abstract method that need to be defined in every class sub of Stream
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")

stream = MemoryStream()
stream.read()