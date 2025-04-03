class CtapiException(Exception):
    name = 'ctapi base exception'

    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def __str__(self):
        return '{name}({code}, {reason})'.format(
                name=self.name,
                code=self.status_code,
                reason=self.reason)
    

class TimeoutError(CtapiException):
    name = 'timeout error'
    

class IamApiError(CtapiException):
    name = 'iam api error'


class ClientRequestError(CtapiException):
    name = 'client request error'


class InternalServerError(CtapiException):
    name = 'internal server error'
