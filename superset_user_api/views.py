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
from flask_appbuilder import expose, ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.sqla.models import User, Role
from superset.views.base import api


class RoleAPIView(ModelView):
    datamodel = SQLAInterface(Role)

    ...


class UserAPIView(ModelView):
    datamodel = SQLAInterface(User)

    @api
    @expose('/users/', methods=['POST'])
    def create_user(self):
        ...

    @api
    @expose('/users/<username>', methods=['DELETE'])
    def delete_user(self, username):
        ...

    @api
    @expose('/users/<username>/roles/', methods=['PUT'])
    def set_user_roles(self, username):
        ...
