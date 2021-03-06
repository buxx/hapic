# -*- coding: utf-8 -*-
import typing

from hapic.description import ControllerDescription
from hapic.description import InputPathDescription
from hapic.description import InputQueryDescription
from hapic.description import InputBodyDescription
from hapic.description import InputHeadersDescription
from hapic.description import InputFormsDescription
from hapic.description import OutputBodyDescription
from hapic.description import OutputHeadersDescription
from hapic.description import ErrorDescription
from hapic.exception import AlreadyDecoratedException


class DecorationBuffer(object):
    def __init__(self) -> None:
        self._description = ControllerDescription()

    def clear(self):
        self._description = ControllerDescription()

    def get_description(self) -> ControllerDescription:
        return self._description

    @property
    def input_path(self) -> InputPathDescription:
        return self._description.input_path

    @input_path.setter
    def input_path(self, description: InputPathDescription) -> None:
        if self._description.input_path is not None:
            raise AlreadyDecoratedException()
        self._description.input_path = description

    @property
    def input_query(self) -> InputQueryDescription:
        return self._description.input_query

    @input_query.setter
    def input_query(self, description: InputQueryDescription) -> None:
        if self._description.input_query is not None:
            raise AlreadyDecoratedException()
        self._description.input_query = description

    @property
    def input_body(self) -> InputBodyDescription:
        return self._description.input_body

    @input_body.setter
    def input_body(self, description: InputBodyDescription) -> None:
        if self._description.input_body is not None:
            raise AlreadyDecoratedException()
        self._description.input_body = description

    @property
    def input_headers(self) -> InputHeadersDescription:
        return self._description.input_headers

    @input_headers.setter
    def input_headers(self, description: InputHeadersDescription) -> None:
        if self._description.input_headers is not None:
            raise AlreadyDecoratedException()
        self._description.input_headers = description

    @property
    def input_forms(self) -> InputFormsDescription:
        return self._description.input_forms

    @input_forms.setter
    def input_forms(self, description: InputFormsDescription) -> None:
        if self._description.input_forms is not None:
            raise AlreadyDecoratedException()
        self._description.input_forms = description

    @property
    def output_body(self) -> OutputBodyDescription:
        return self._description.output_body

    @output_body.setter
    def output_body(self, description: OutputBodyDescription) -> None:
        if self._description.output_body is not None:
            raise AlreadyDecoratedException()
        self._description.output_body = description

    @property
    def output_headers(self) -> OutputHeadersDescription:
        return self._description.output_headers

    @output_headers.setter
    def output_headers(self, description: OutputHeadersDescription) -> None:
        if self._description.output_headers is not None:
            raise AlreadyDecoratedException()
        self._description.output_headers = description

    @property
    def errors(self) -> typing.List[ErrorDescription]:
        return self._description.errors

    def add_error(self, description: ErrorDescription) -> None:
        self._description.errors.append(description)
