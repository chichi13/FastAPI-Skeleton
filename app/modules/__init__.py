import pathlib
import pkgutil
from importlib import import_module
from importlib.util import find_spec


def _modules(postfix="") -> list:
    """
    Récupère la liste des modules du package "modules", on peut
    spécifier un prefix (ex : '.views') pour importer (s'il existe) un sous-module
    :param postfix: le sous-module d'un module à importer
    :return: la liste de tous les modules (ou sous module si spécifiés) trouvés
    """
    return [
        import_module(f".{name}{postfix}", package=__name__)
        for (_, name, _) in pkgutil.iter_modules([str(pathlib.Path(__file__).parent)])
        if find_spec(f".{name}{postfix}", package=__name__)
    ]


def detect_models():
    _modules(".models")
