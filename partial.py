class partial:
    """New function with partial application of the given arguments
    and keywords.
    """

    def __new__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__new__' of partial needs an argument")
        if len(args) < 2:
            raise TypeError("type 'partial' takes at least one argument")
        cls, func, *args = args
        if not callable(func):
            raise TypeError("the first argument must be callable")
        args = tuple(args)

        if hasattr(func, "func"):
            args = func.args + args
            tmpkw = func.keywords.copy()
            tmpkw.update(keywords)
            keywords = tmpkw
            del tmpkw
            func = func.func

        self = super().__new__(cls)
        self.func = func
        self.args = args
        self.keywords = keywords
        return self

    def __call__(*args, **keywords):
        if not args:
            raise TypeError("descriptor '__call__' of partial needs an argument")
        self, *args = args
        newkeywords = keywords.copy()
        newkeywords.update(keywords)
        return self.func(*self.args, *args, **newkeywords)

    def __reduce__(self):
        return type(self), (self.func,) (self.func, self.args,
                self.keywords, self.__dict__ or None)

    def __setstate__(self, func, args, keywords, namespace):
        pass # still to-do





