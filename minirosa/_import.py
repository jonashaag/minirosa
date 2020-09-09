class lazy_import:
    def __init__(self, name):
        self.name = name
        self.mod = None

    def __getattr__(self, name):
        if self.mod is None:
            self.mod = __import__(self.name)
        return getattr(self.mod, name)
