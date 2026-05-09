# ckb-next — Mode Shift Fork

A fork of [ckb-next](https://github.com/ckb-next/ckb-next) adding **hold-to-shift mode** functionality to the Special binding tab.

> **Base version:** ckb-next v0.6.2  
> **Fork by:** [storymode-exe](https://github.com/storymode-exe)

---

## What's New

### Trigger on Release
Bind a key to switch modes **on key release** instead of key press.

### Retain Original Key Function
Check this to keep the key's original function while also switching modes — the key still types/acts normally, it *also* switches modes.

### Fixed: Unchecking Mode Clears Binding
Previously, unchecking "Switch to mode" and clicking Apply would leave the old binding in place. Now it properly clears.

---

## Hold-to-Shift Mode Behavior

The combination of these two options enables **hold-to-shift** — a key that temporarily shifts to a different mode while held, and reverts when released:

**Mode A** — bind your key to:
- Switch to Mode B
- ✅ Retain original key function

**Mode B** — bind the same key to:
- Switch to Mode A
- ✅ Trigger on release
- ✅ Retain original key function

Now holding the key shifts to Mode B. Releasing it shifts back to Mode A. The key still works normally the whole time.

### Star Citizen Example
- **Mode 1** — Default SC lighting
- **Mode 2** — Flight mode (highlights WASD, QE, flight keys)

Bind **Left Alt** in Mode 1: Switch to Mode 2, on press, retain function  
Bind **Left Alt** in Mode 2: Switch to Mode 1, on release, retain function

Hold Alt → flight mode colors. Release → back to normal. Alt still works in-game throughout.

---

## Screenshots

<!-- Add screenshots here after building -->

**Special tab — new options:**

![Special tab showing new checkboxes](screenshots/mode_shift_1.png)

![Mode shift in action](screenshots/mode_shift_2.png)

---

## Building from Source

### Requirements
- cmake
- gcc / g++
- Qt6 development packages
- libusb1
- systemd (libudev)
- zlib
- QuaZip (Qt6)
- xcb-util-wm
- wayland-protocols

### Fedora / Bazzite (via distrobox)

```bash
# Create a build container
distrobox create --name ckb-dev --image fedora:43
distrobox enter ckb-dev

# Install dependencies
sudo dnf install -y cmake gcc-c++ qt6-qtbase-devel qt6-qttools-devel \
    libusb1-devel systemd-devel zlib-devel git \
    quazip-qt6-devel xcb-util-wm-devel wayland-protocols-devel

# Clone and build
git clone https://github.com/storymode-exe/ckb-next
cd ckb-next
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

The GUI binary will be at `build/bin/ckb-next`.

### Installing

The ckb-next **daemon** (`ckb-next-daemon`) handles USB communication and runs as a system service. You only need to replace the **GUI** binary — the daemon from your distro's package is compatible.

```bash
# Stop the current GUI
pkill ckb-next

# Copy the new binary (adjust path as needed)
sudo cp build/bin/ckb-next /usr/bin/ckb-next

# Restart
ckb-next --background
```

> **Bazzite note:** `/usr` is immutable. Copy the binary to `~/.local/bin/` instead and update your autostart entry.

---

## Upstream

This fork tracks [ckb-next/ckb-next](https://github.com/ckb-next/ckb-next) at v0.6.2.  
A PR to upstream is planned once the feature is stable.

---

## License

GPL v2 — same as upstream ckb-next.
