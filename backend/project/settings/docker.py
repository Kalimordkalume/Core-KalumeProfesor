if IN_DOCKER:
    print("Running IN_DOCKER mode...")
    assert MIDDLEWARE[:1] == [
        "django.middleware.security.SecurityMiddleware",
    ]
