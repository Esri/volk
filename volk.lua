project "volk"

dofile(_BUILD_DIR .. "/static_library.lua")

configuration { "*" }

uuid "8FDDA7C9-8542-4B3A-95EC-C107FEAC55F6"

includedirs {
  _3RDPARTY_DIR .. "/Vulkan-Headers/include",
}

files {
  "volk.h",
  "volk.c",
}

if (_PLATFORM_WINDOWS) then
  defines {
    "VK_USE_PLATFORM_WIN32_KHR",
  }
elseif (_PLATFORM_LINUX) then
  defines {
    "VK_USE_PLATFORM_XLIB_KHR",
  }
end
