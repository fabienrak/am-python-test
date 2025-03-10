template = {
    "swagger": "2.0",
    "info": {
        "title": "TASK API",
        "description": "API for amltd task",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "mdgredteam@gmail.com",
            "url": "https://fabienrak.github.io",
        },
        "termsOfService": "https://fabienrak.github.io",
        "version": "1.0"
    },
    "basePath": "",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
