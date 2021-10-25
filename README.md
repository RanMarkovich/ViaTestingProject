Project tree:

```
-- tests
    |-- __init__.py
    |-- common_fucntions.py
    |-- conftest.py
    |-- services
    |   |-- __init__.py
    |   `-- user_service
    |       |-- __init__.py
    |       |-- config.py
    |       |-- data
    |       |   |-- user_creation_payload.json
    |       |   `-- user_creation_resp_payload.json
    |       |-- helpers
    |       |   |-- __init__.py
    |       |   |-- service_data_factory.py
    |       |   `-- service_test_helper.py
    |       `-- test_user_service.py
    `-- test_utils.py``
```

<h3> Run tests:</h3> 
<h4> pre-requisites: </h4> 
Installed packages: pytest, requests

Run command:
```pytest tests/services/user_service```