#!usr/bin/env python3
#Copyright (c) Podmogilniy Ivan

''' Module decription '''

import os
import pickle
import copy

class ImageError(Exception): pass
class CoordinateError(ImageError): pass
class LoadError(ImageError): pass
class SaveError(ImageError): pass
class ExportError(ImageError): pass
class NoFilenameError(ImageError): pass

class Image:
    def __init__(self, width, height, filename = '', background = '#FFFFFF'):
        self.filename = filename
        self.__width = width
        self.__height = height
        self.__background = background
        self.__data = {}
        self.__colors = {self.__background}
        
    @property
    def background(self):
        return self.__background
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def data(self):
        return self.__data
    @property
    def color(self):
        return self.__colors
    
    def __getitem__(self, coordinate):
        assert len(coordinate) == 2, 'coordinate must be a 2-tuple'
        if (not(0 <= coordinate[0] <= self.width) or
            not(0 <=coordinate[1] <= self.height)):
            raise CoordinateError(str(coordinate))
        return self.__data.get(tuple(coordinate), self.__background)

    def __setitem__(self, coordinate, color):
        assert len(coordinate) == 2, 'coordinate should be a 2-tuple'
        if (not(0 <= coordinate[0] <= self.width) or
                    not(0 <= coordinate[1] <= self.height)):
            raise CoordinateError(str(coordinate))
        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)

    def __delitem__(self, coordinate):
        assert len(coordinate) == 2, 'coordinate must be a 2-tuple'
        if (not(0 <= coordinate[0] <= self.width) or
            not(0 <= coordinate[1] <= self.height)):
            raise CoordinateError()
        self.__data.pop(tuple(coordinate), None)

    def save(self, filename = None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()
        fh = None
        try:
            data = [self.width, self.height, self.__background, self.__data]
            fh = open(filename, 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self, filename = None):
        if filename is not None:
            self.filename = filename
        if not self.filename:
            raise NoFilenameError()
        fh = None
        try:
            fh = open(filename, 'rb')
            data = pickle.load(fh)
            (self.__width, self.__height, self__background,
                 self.__data) = data
            self.__colors = set(self.__data.values()) | {self.__background}
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def export(self, filename = None):
        if filename.lower().endswith('.xpm'):
            self.__export_xpm(filename)
        else:
            ExportError("unsupported export format: " +
                            os.path.splitext(filename)[1])

    def resize(self, width=None, height=None):
        """ Resize the Image to given width and height

        If 'width' is None, the Image width do not changes,
        if 'height' is None the Image height do not changes

        >>> img = Image(50, 50)
        >>> img.resize(25, 25)
        True
        >>> img[50, 50]
        Traceback (most recent call last):
        ...
        CoordinateError: (50, 50)
        >>> img.resize()
        False
        """
        if width is None and height is None:
            return False
        if width is None:
            width = self.__width
        if height is None:
            height = self.__heigt
        if height >= self.__height and width >= self.__width:
            self.__height = height
            self__width = width
            return True
        self__height = height
        self__widht = width
        for x, y in list(self.__data.key()):
            if x >= width or y >= height:
                del self.__data[(x, y)]
        self.__colors = set(self.__data.values()) | {self.__background}
        return True
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
            
        











