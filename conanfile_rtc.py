#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile


class VolkConan(ConanFile):
    name = "volk"
    version = "1.3.275"
    url = "https://github.com/Esri/volk/blob/runtimecore/"
    license = "https://github.com/Esri/volk/blob/runtimecore/LICENSE.md"
    description = ("Volk is a meta-loader for Vulkan")
    
    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/volk/"

        # headers
        self.copy("*.h*", src=base, dst=relative)
