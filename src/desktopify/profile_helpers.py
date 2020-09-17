import json
import os
import time

from pathlib import Path


def create_profile_if_not_exist(profile_full_path: str) -> None:
    Path(profile_full_path).mkdir(parents=True, exist_ok=True)

    create_times_json_file_if_not_exist(profile_full_path)
    create_user_chrome_css_file_if_not_exist(profile_full_path)
    create_user_js_file_if_not_exist(profile_full_path)


def create_times_json_file_if_not_exist(profile_full_path: str) -> None:
    file_name = os.path.join(profile_full_path, "times.json")

    if os.path.exists(file_name):
        return

    with open(file_name, "w") as f:
        file_content = {
            "created": get_timestamp_in_milliseconds(),
            "firstUse": None
        }

        json.dump(file_content, f)


def create_user_chrome_css_file_if_not_exist(profile_full_path: str) -> None:
    parent_dir_name = os.path.join(profile_full_path, "chrome")
    Path(parent_dir_name).mkdir(parents=True, exist_ok=True)

    file_name = os.path.join(parent_dir_name, "userChrome.css")

    if os.path.exists(file_name):
        return

    with open(file_name, "w") as f:
        file_content = "#nav-bar, #identity-box, #tabbrowser-tabs, #TabsToolbar { visibility: collapse !important; }"
        f.write(file_content)


def create_user_js_file_if_not_exist(profile_full_path: str) -> None:
    file_name = os.path.join(profile_full_path, "user.js")

    if os.path.exists(file_name):
        return

    with open(file_name, "w") as f:
        file_content = """
user_pref("browser.cache.disk.enable", false);
user_pref("browser.cache.disk.capacity", 0);
user_pref("browser.cache.disk.filesystem_reported", 1);
user_pref("browser.cache.disk.smart_size.enabled", false);
user_pref("browser.cache.disk.smart_size.first_run", false);
user_pref("browser.cache.disk.smart_size.use_old_max", false);
user_pref("browser.ctrlTab.previews", true);
user_pref("browser.tabs.warnOnClose", false);
user_pref("plugin.state.flash", 2);
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);"""
        f.write(file_content)


def get_timestamp_in_milliseconds() -> int:
    return int(round(time.time() * 1000))
