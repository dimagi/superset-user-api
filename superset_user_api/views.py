"""
API views for ``User`` and ``Role``.

Example usage::

    $ curl -X POST \
        -H x-superset-user-api-key="$API_KEY" \
        -d username=testy@example.com \
        -d first_name=Testy \
        -d last_name=McTestface \
        -d email=testy@example.com \
        -d roles=my-test-space \
        -d roles=my-live-space \
        https://superset.example.com/api/users/

To add or remove roles to/from a user, use a PUT request to a "roles"
endpoint on the user, and include all of the user's roles. To remove the
"my-live-space" role from the user given in the example above, use ::

    $ curl -X PUT \
        -H x-superset-user-api-key="$API_KEY" \
        -d roles=my-test-space \
        https://superset.example.com/api/users/testy@example.com/roles/

.. note::
   The "my-live-space" role was removed from the user by omitting it
   from the request.

"""
from flask_appbuilder.api import ModelRestApi, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.sqla.models import User, Role
from superset import appbuilder


class RoleAPIView(ModelRestApi):
    resource_name = 'role'
    datamodel = SQLAInterface(Role)

    allow_browser_login = True

    # search_filters = {"name": [CustomFilter]}
    openapi_spec_methods = {
        "get_list": {
            "get": {
                "description": "Get roles",
            }
        }
    }


appbuilder.add_api(RoleAPIView)


class UserAPIView(ModelRestApi):
    resource_name = 'user'
    datamodel = SQLAInterface(User)
    allow_browser_login = True


appbuilder.add_api(UserAPIView)
