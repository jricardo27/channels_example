from functools import wraps

import os
import shelve


class PersistentList(list):
    """
    A list that is persisted to a file every time it is modified.

    This list is not thread safe.
    """

    KEY = 'internal_list'
    _skip_save = False
    _skip_load = False

    MODIFIERS = [
        'append', 'clear', 'extend', 'insert', 'pop', 'remove', 'reverse',
        'sort',
    ]

    GETTERS = ['copy', 'count', 'index']

    def __init__(self, filename, clear_file=False, *args, **kwargs):
        self.filename = filename

        # Decorate modifier methods so they persist after modifying the list.
        for attr in self.MODIFIERS:
            setattr(self, attr, self._autosave(getattr(self, attr)))

        # Decorate getter methods so they load the file before hand.
        for attr in self.GETTERS:
            setattr(self, attr, self._autoload(getattr(self, attr)))

        super().__init__(*args, **kwargs)

        if clear_file:
            try:
                os.remove(self.filename)
            except OSError:
                pass
        else:
            # Load any previous persisted data.
            self._load(clear_before_load=False)

    def _autosave(self, func):
        """Decorate the modifier methods."""

        @wraps(func)
        def _func(*args, **kwargs):
            """Perform the action over the data, then persist."""
            ret = func(*args, **kwargs)

            self._save()

            return ret
        return _func

    def _save(self):
        """Persist the list to a file."""
        if self._skip_save:
            return

        storage = shelve.open(self.filename)

        self._skip_load = True
        storage[self.KEY] = list(self)
        self._skip_load = False

        storage.close()

    def _autoload(self, func):
        """Decorate the getter methods."""

        @wraps(func)
        def _func(*args, **kwargs):
            """
            Load the data from the file, then perform the action over it.
            """
            self._load(clear_before_load=True)

            ret = func(*args, **kwargs)

            return ret
        return _func

    def _load(self, clear_before_load=False):
        """Load persisted data."""

        if self._skip_load:
            return

        self._skip_save = True

        if clear_before_load:
            self.clear()

        storage = shelve.open(self.filename)
        self.extend(storage.get(self.KEY, []))
        storage.close()

        self._skip_save = False

    # The following attributes couldn't be overridden using `setattr`

    def __getitem__(self, item):
        self._load(clear_before_load=True)

        return super().__getitem__(item)

    def __setitem__(self, index, value):
        super().__setitem__(index, value)

        self._save()

    def __delitem__(self, index):
        super().__delitem__(index)

        self._save()

    def __add__(self, value):
        super().__add__(value)

        self._save()

    def __contains__(self, *args, **kwargs):
        self._load(clear_before_load=True)

        return super().__getitem__(*args, **kwargs)

    def __len__(self):
        self._load(clear_before_load=True)

        return super().__len__()

    def __iter__(self):
        self._load(clear_before_load=True)

        return super().__iter__()

    def __repr__(self):
        self._load(clear_before_load=True)

        return super().__repr__()

    def __eq__(self):
        self._load(clear_before_load=True)

        return super().__eq__()
