#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile


class VolkConan(ConanFile):
    name = "volk"
    version = "1.3.275"
    url = "https://github.com/Esri/volk/blob/runtimecore/"
    license = "https://github.com/Esri/volk/blob/runtimecore/LICENSE.md"
    description = ("Volk is a meta-loader for Vulkan")
    
    # RTC specific triple
    settings = "platform_architecture_target"
    
    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/volk/"

        # headers
        self.copy("*.h*", src=base, dst=relative)

        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
