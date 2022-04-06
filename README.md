# Reqplus :heavy_plus_sign:
### _A lib for strict Flask reqparse_

This is an easy way to raise required parameters using reqparse from Flask Restful framework.

## Installation
```sh
pip install reqplus
```

### Required
- [Python >= 3.7](https://www.python.org/downloads/release/python-370/) - Python is required
- Pip is required
- [Flask-RESTful 0.3.9](https://flask-restful.readthedocs.io/en/latest/) Flask Restful

## Development

1- Create a normal reqparse object
```py
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=True, location='args', help='Id is required')
```

2- Insteated using `parse_args` replace it for `pre_parse_args`,
StrictParser is required for use `pre_parse_args`
```py
from flask_restful import reqparse
from reqplus import StrictParser

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, required=True, location='args', help='Id is required')

# Old one >>> args = parser.parse_args()
args = StrictParser.pre_parse_args(parser)
```

`pre_parse_args` will return a dictionary with the values from the request like a normal reqparse implementation, if one parameter is required and isn't in the request `pre_parse_args` will raise an exception with the `help` message you set.

> Take care using required parameters, for required parameters you have to set the help parameter to display correctly the message.

In a normal reqparse implementation you will use the next structure:

```py
# Taked from the official documentation
from flask_restful import reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('foo', type=int, required=True, help='foo error message')
parser.add_argument('bar', type=int, required=True, help='bar error message')

# Error response
{
    "message":  {
        "foo": "foo error message",
        "bar": "bar error message"
    }
}
```

With this implementation you will get an object named "message" inside another object named "data" with every error message with a key named equal to the parameter name, for this case you have to validate in the exception section looking for an easy way to return this values.

Normally an API returns static messages doing "try cath" blocks for raise all the incoming exceptions and returning messages like the following example:
> "message" :  "foo error message"

With reqparse you will have the following message:
> "message" : "400 Bad Request: The browser (or proxy) sent a request that this server could not understand."

To improve this error reqplus intercept the incoming request and comparate it with de reqparse arguments raising an exception if any argument don't meet the conditions.

`pre_parse_args` also accept the current parameters from reqparse and include a new parameter name `bundle` if you want to bundle all the error from de validation in one exception

### Example

```py
# strict=True
# http_error_code=400
# New bundle=True
args = StrictParser.pre_parse_args(parser, strict=True, http_error_code=400, bundle=True)
```

Set bundle in false to get the first posible error

```py
# Old
"message":  {
    "foo" : "foo error message",
    "bar" : "bar error message"
}

# New 
# bundle:false
"message" : "foo error message"
# bundle:true
"message" : "foo error message, bar error message"
```

# Comments
Any recomendation is acepted.

# Licence
GNU - Yeah baby!