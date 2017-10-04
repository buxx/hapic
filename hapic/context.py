# -*- coding: utf-8 -*-
import json
import typing
from http import HTTPStatus

import bottle

from hapic.exception import OutputValidationException
# from hapic.hapic import _default_global_error_schema
from hapic.processor import RequestParameters, ProcessValidationError


class ContextInterface(object):
    def get_request_parameters(self, *args, **kwargs) -> RequestParameters:
        raise NotImplementedError()

    def get_response(
        self,
        response: dict,
        http_code: int,
    ) -> typing.Any:
        raise NotImplementedError()

    def get_validation_error_response(
        self,
        error: ProcessValidationError,
        http_code: HTTPStatus=HTTPStatus.BAD_REQUEST,
    ) -> typing.Any:
        raise NotImplementedError()


class BottleContext(ContextInterface):
    def get_request_parameters(self, *args, **kwargs) -> RequestParameters:
        return RequestParameters(
            path_parameters=bottle.request.url_args,
            query_parameters=bottle.request.params,
            body_parameters=bottle.request.json,
            form_parameters=bottle.request.forms,
            header_parameters=bottle.request.headers,
        )

    def get_response(
        self,
        response: dict,
        http_code: int,
    ) -> bottle.HTTPResponse:
        return bottle.HTTPResponse(
            body=json.dumps(response),
            headers=[
                ('Content-Type', 'application/json'),
            ],
            status=http_code,
        )

    def get_validation_error_response(
        self,
        error: ProcessValidationError,
        http_code: HTTPStatus=HTTPStatus.BAD_REQUEST,
    ) -> typing.Any:
        # TODO
        from hapic.hapic import _default_global_error_schema
        unmarshall = _default_global_error_schema.dump(error)
        if unmarshall.errors:
            raise OutputValidationException(
                'Validation error during dump of error response: {}'.format(
                    str(unmarshall.errors)
                )
            )

        return bottle.HTTPResponse(
            body=json.dumps(unmarshall.data),
            headers=[
                ('Content-Type', 'application/json'),
            ],
            status=int(http_code),
        )
