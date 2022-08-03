class Image:
    def show(self) -> str:
        return "Image"


class RemoteImage(Image):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass


class DiskImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self) -> str:
        return "Disk Image"


class InternetImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self) -> str:
        return "Internet Image"


class ImageProxy(Image):
    def __init__(self, remote_image: RemoteImage):
        self._remote_image = remote_image

    def show(self) -> str:
        if not self._remote_image.is_loaded():
            self._remote_image.load_from_source()
        return self._remote_image.show()


if __name__ == '__main__':
    disk_image_proxy = ImageProxy(DiskImage())
    internet_image_proxy = ImageProxy(InternetImage())

    print(disk_image_proxy.show())
    print(internet_image_proxy.show())
