class NonPositiveError(BaseException):
    pass

class PositiveList(list):
    def append(self, o) -> None:
        if o > 0:
            return super(PositiveList, self).append(o)
        else:
            raise NonPositiveError

