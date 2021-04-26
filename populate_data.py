import os
import django


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
    django.setup()
    from projects.utils import populate_data

    print("Populating data...")
    populate_data.projects()


if __name__ == "__main__":
    main()
