# check if navis is installed, otherwise do not import this module
# if navis is installed, then import the module
# if not, then do not import the module

try:
    import navis

    from .navis import treeneuron_to_networkframe

    __all__ = ["treeneuron_to_networkframe"]
except ImportError:
    raise UserWarning(
        "navis is not installed. Please install navis to use the navis module. This can"
        "be done by running `pip install neurovista[navis]` in the terminal."
    )
