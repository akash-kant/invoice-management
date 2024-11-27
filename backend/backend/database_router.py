class YourDatabaseRouter:
    def db_for_read(self, model, **hints):
        """Direct read queries to the appropriate database."""
        if model._meta.app_label == 'your_mongodb_app':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direct write queries to the appropriate database."""
        if model._meta.app_label == 'your_mongodb_app':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if both objects are in the same database."""
        db_set = {'default', 'mongodb'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Direct migrations for specific apps to the right database."""
        if app_label == 'your_mongodb_app':
            return db == 'mongodb'
        return db == 'default'
