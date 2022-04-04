from flask import request
from flask_restful import reqparse
from re import match

class StrictParser(reqparse.RequestParser):

    def pre_parse_args(self, req_in=None, strict_in=False, http_error_code_in=400, bundle=False):
        """
        Overide reqparse parser in order to validate each of the incoming request parameters
        """
        try:
            if req_in is None:
                req_in = request
            
            #args and values are query params (args recommend)
            query_params = list(req_in.args.keys())
            #form are Form and Form-Encode params
            form_params = list(req_in.form.keys())
            #headers.environ for header variables and concat 'HTTP_' + var_name in upper case
            header_params = [i for i in list(req_in.headers.environ.keys()) if 'HTTP_' in i] 
            #files for files
            file_params = list(req_in.files.keys())

            errors = []

            for arg in self.args:
                if arg.required:
                    if arg.location == 'args':
                        if not arg.name in query_params: errors.append(arg.help)
                    if arg.location == 'form':
                        if not arg.name in form_params: errors.append(arg.help)
                    if arg.location == 'headers':
                        if not 'HTTP_' + str(arg.name).upper() in header_params: errors.append(arg.help)
                    if arg.location == 'files':
                        if not arg.name in file_params: errors.append(arg.help)
            
            if errors != []:
                if bundle:
                    raise Exception(', '.join(errors))
                raise Exception(errors[0])

            return reqparse.RequestParser.parse_args(self, req_in, strict_in, http_error_code_in)
        except Exception as e:
                raise Exception(str(e))