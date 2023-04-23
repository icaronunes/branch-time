class GitRepositoryError(Exception):
    def __init__(self, message, cod=666) -> None:
        self.message = "fatal: not a git repository (or any of the parent directories):"
        self.cod = cod
        super().__init__(message)
