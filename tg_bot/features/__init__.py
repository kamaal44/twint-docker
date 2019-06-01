from os.path import dirname, basename, isfile
import glob
path = glob.glob(dirname(__file__) + "/*.py")
__all__ = [ basename(f)[:-3] for f in path if isfile(f) and f.endswith(".py") and not f.endswith('__init__.py')]