# -*- coding: utf-8 -*-

from fastapi.responses import UJSONResponse

from pynaja.common.struct import Result, Const
from pynaja.enum.base_enum import Enum


class RespCode(Enum):
    Success = 0  # 成功
    Unknown = -1  # 未知


RespMessage = Const()
RespMessage[RespCode.Success] = r"成功"
RespMessage[RespCode.Unknown] = r"未知"


class Response(UJSONResponse):

    def render(self, content):
        return super().render(Result(code=RespCode.Success, data=content, msg=RespMessage[RespCode.Success]))


class ErrorResponse(Exception, UJSONResponse):

    def __init__(self, error_code, content=None, status_code=200, details=None, **kwargs):
        self._error_code = error_code
        self._details = details

        Exception.__init__(self)
        UJSONResponse.__init__(self, content, status_code, **kwargs)

    def render(self, content):
        return super().render(
            Result(code=self._error_code, data=content, msg=RespMessage[self._error_code], details=self._details)
        )
