import ConfigParser
import BL_Exit


class BL_Exit_Theme():
        def __init__(self, theme, settings, blexit):
            self.theme = theme
            self.settings = settings
            self.blexit = blexit

        def set_detail(self, key, value):
            self.settings[key] = value

        def set_details_from_config(self, cp, default_theme):
            for key in default_theme_settings.iterkeys():
                default_theme_detail = default_theme_settings[key]
                try:
                    config_value = cp.get(self.theme, key)
                except ConfigParser.NoOptionError as e:
                    msg = "theme config option {} is not set for theme {}"
                    BL_Exit.on_debug(msg.format(key, self.theme))
                    config_value = None
                    pass
                if config_value is not None:
                    if default_theme_detail.value_type == 'int':
                        try:
                            config_value = int(config_value)
                        except:
                            msg = "theme config option {} is not an int"
                            self.blexit.on_debug(msg.format(key, self.theme))
                            config_value = default_theme_detail.value
                    elif default_theme_detail.value_type == 'float':
                        try:
                            default_theme_detail.config_value = float(config_value)
                        except:
                            msg = "theme config option {} is not a float"
                            self.bl-exit.on_debug(msg.format(key, self.theme))
                            config_value = default_theme_detail.value
                else:
                    if default_theme_detail.required:
                        config_value = default_theme_detail.value
                if config_value is not None:
                    self.set_detail(key, config_value)
