#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class File_Crolla():

    def __init__(self):
        self.path_list = []
        self.info_list = []

    def File_Path_Getter(self, Path, Extension):
        """与えられたPath以下にある，Extensionで指定された拡張子を持つ
        全てのファイルの絶対パスをリストにして返す"""

        if os.path.isdir(Path) and os.path.splitext(Path)[1] != Extension:
            for sub_dir in os.listdir(Path):
                next_path = Path + "/" + sub_dir
                self.File_Path_Getter(next_path, Extension)
        elif os.path.splitext(Path)[1] == Extension:
            self.path_list.append(Path)

    def return_dir_list(self):
        return self.path_list


if __name__ == '__main__':

    Crolla = File_Crolla()
    base_path = ""
    extension = ".txt"

    Crolla.File_Path_Getter(base_path, extension)
    dir_list = Crolla.return_dir_list()
