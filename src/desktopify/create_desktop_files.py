import os

from typing import List

from .icon_helpers import download_icon_if_not_exist
from .models import Entry
from .path_helpers import get_icon_file_full_path, get_profile_full_path, get_application_file_path, get_wm_class_name
from .profile_helpers import create_profile_if_not_exist


def create_desktop_files(desktopify_path: str, applications_path: str, entries: List[Entry]):
    for entry in entries:
        application_file_path = get_application_file_path(applications_path, entry.name)

        create_entry_if_not_exist(desktopify_path, entry, application_file_path)


def create_entry_if_not_exist(desktopify_path: str, entry: Entry, application_file: str):
    if os.path.exists(application_file):
        return

    icon_path = get_icon_file_full_path(desktopify_path, entry.name)
    download_icon_if_not_exist(entry.icon_url, icon_path)

    profile_path = get_profile_full_path(desktopify_path, entry.name)
    create_profile_if_not_exist(profile_path)

    file_content = template.format(
        name=entry.name,
        description=entry.description,
        url=entry.url,
        wm_class_name=get_wm_class_name(entry.name),
        profile_path=profile_path,
        icon_file=icon_path
    )

    with open(application_file, "w") as f:
        f.write(file_content)


template = """
[Desktop Entry]
Name={name}
Name[en_US]={name}
Comment={description}
Encoding=UTF-8
Terminal=false
Type=Application
Exec=firefox --class {wm_class_name} --profile {profile_path} {url}
Icon={icon_file}
StartupWMClass={wm_class_name}
StartupNotify=true
"""
