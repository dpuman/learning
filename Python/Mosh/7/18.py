from abc import ABC, abstractmethod


class Stream(ABC):
    def open(self):
        print("open")

    def close(self):
        print("open")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("do")


class NetworkStream(Stream):
    pass


# CANT create object of abc
# fs = Stream()
# ns = NetworkStream()
fs = FileStream()
fs.open()
