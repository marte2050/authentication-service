def test_get_permission_by_id(permission_service, create_permission):
    permission_id = 1
    permission = permission_service.get_permission_by_id(permission_id)
    assert permission is not None


def test_get_permission_by_name(permission_service, create_permission):
    name = "testpermission"
    permission = permission_service.get_permission_by_name(name)
    assert permission is not None


def test_create_permission(permission_service):
    permission_data = {
        "name": "newpermission",
        "description": "A new permission",
    }

    permission = permission_service.create_permission(permission_data)
    assert permission is not None


def test_update_permission(permission_service, create_permission):
    permission_id = 1
    permission_data = {
        "name": "updatedpermission",
        "description": "An updated permission",
    }

    permission = permission_service.update_permission(permission_id, permission_data)
    assert permission.name == "updatedpermission"
    assert permission.description == "An updated permission"


def test_delete_permission(permission_service, create_permission):
    permission_id = 1
    result = permission_service.delete_permission(permission_id)
    assert result == {"detail": "Permission deleted successfully."}
