import os

from pathlib import Path


def get_profile_full_path(desktopify_path: str, app_name: str) -> str:
    profile_name = "-".join(app_name.split(" "))

    return f"{desktopify_path}/profiles/{profile_name}"


def get_icon_file_full_path(desktopify_path: str, app_name: str) -> str:
    file_name = "-".join(app_name.split(" "))

    return f"{desktopify_path}/assets/{file_name}.png"


def get_application_file_path(applications_path: str, app_name: str) -> str:
    file_name = "-".join(app_name.split(" "))

    return f"{applications_path}/{file_name}.desktop"


def get_wm_class_name(app_name: str) -> str:
    class_name = "-".join(app_name.split(" "))

    return f"Desktopify-{class_name}"
