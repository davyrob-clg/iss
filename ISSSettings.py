

import sqlite3

class ISSettings:

    database_name = "iss_data.db"

    """
    ISS Settings Class - will allow any settings to be saved to the 
    SQL lite settings database which 

    It provides a brief overview of what the class does.
    This class is designed to demonstrate class documentation.
    """

    # Class attributes (shared by all instances)
    class_attribute = "This is a class-level attribute."

    def __init__(self, param1, param2):
        # Instance attributes (unique to each instance)
        self.param1 = param1
        self.param2 = param2
        self.derived_attribute = f"Combination: {param1} and {param2}"

    def instance_method(self):
        """
        An instance method that operates on instance attributes.
        """
        return f"Instance method called. Param1: {self.param1}, Param2: {self.param2}"

    @classmethod
    def class_method(cls):
        """
        A class method that operates on class attributes.
        It receives the class itself (cls) as the first argument.
        """
        return f"Class method called. Class attribute: {cls.class_attribute}"

    @staticmethod
    def static_method(arg):
        """
        A static method that does not operate on instance or class attributes.
        It does not receive self or cls as an argument.
        """
        return f"Static method called with argument: {arg}"


    def save_setting(setting_name, setting_value):
        """Saves or updates a single setting in the SQLite database."""
        conn = sqlite3.connect('app_settings.db')
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                name TEXT PRIMARY KEY,
                value TEXT
            )
        ''')

        # Insert or update the setting
        cursor.execute('''
            INSERT OR REPLACE INTO settings (name, value) VALUES (?, ?)
        ''', (setting_name, setting_value))

        conn.commit()
        conn.close()


    def get_setting(setting_name, default_value=None):
        """Retrieves a setting from the SQLite database."""
        conn = sqlite3.connect('iss_data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT value FROM settings WHERE name = ?',
                    (setting_name,))
        result = cursor.fetchone()

        conn.close()

        if result:
            return result[0]
        else:
            return default_value


# Example usage:
if __name__ == "__main__":

    iss_settings = ISSettings()

    # Save some settings
    iss_settings.save_setting('theme', 'dark')
    iss_settings.save_setting('font_size', '14px')
    iss_settings.save_setting('username', 'user123')

    # Retrieve settings
    theme = iss_settings.get_setting('theme', 'light')
    font_size = iss_settings.get_setting('font_size', '12px')
    # Setting not found, uses default
    password = iss_settings.get_setting('password', 'not_set')

    print(f"Theme: {theme}")
    print(f"Font Size: {font_size}")
    print(f"Password: {password}")

    # Update a setting
    iss_settings.save_setting('theme', 'light')
    updated_theme = iss_settings.get_setting('theme')
    print(f"Updated Theme: {updated_theme}")
