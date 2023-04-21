from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from dal.models.user import User
class Container(containers.DeclarativeContainer):

    user = providers.Factory(
        User,
        "Kendriya Vidhyala",
        "C.B.S.E.",
        "Bina"
    )

    # student = providers.Factory(
    #     Student,
    #     "Siddhartha",
    #     28, 12,
    #     school
    # )