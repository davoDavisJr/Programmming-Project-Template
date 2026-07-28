# FIT1045 Environment Check

Use this checklist to confirm the C++ profile can build on your device.

1. Open the terminal required by your class environment.
2. Confirm a compiler is available:

```powershell
clang++ --version
```

3. Build the starter program:

```powershell
make
```

4. Run the program:

```powershell
./build/main
```

On Windows, the output file may be `build/main.exe`.

If you use MSYS2 MINGW64, open the matching terminal before running these
commands. If you use SplashKit, confirm that your local SplashKit setup exposes
the compiler wrapper or flags required by your class.
