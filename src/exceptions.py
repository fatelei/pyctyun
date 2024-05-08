from rest_framework.response import Response

class CtapiException(Exception):
    name = 'iam exception'

    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def __str__(self):
        return '{name}({code}, {reason})'.format(
                name=self.name,
                code=self.status_code,
                reason=self.reason)

    @property
    def data(self):
        return {
            'statusCode': 900,
            'message': self.reason,
            'description': '请求失败',
            'errorCode': 'Openapi.Ctiam.Error',
            'error': 'Openapi.Ctiam.Error'
        }

    def response(self):
        return Response(data=self.data, status=200)
    

class TimeoutError(CtapiException):
    name = 'timeout error'
    

class IamApiError(CtapiException):
    name = 'iam api error'


class ClientRequestError(CtapiException):
    name = 'client request error'


class InternalServerError(CtapiException):
    name = 'internal server error'
