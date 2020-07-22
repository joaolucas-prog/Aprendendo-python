class ExtratorArgumentosUrl:

    def __init__(self,url):
        if self.isUrl(url):
            self.url = url
        else:
            raise LookupError ("URL Invalida !!!!!!!")

    @staticmethod
    def isUrl(url):
        if url:
            return True
        else:
            return False