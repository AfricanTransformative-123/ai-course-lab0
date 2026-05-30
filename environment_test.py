import sys
import platform
import os

def verify_environment():

    results = []

    python_version = sys.version.split()[0]
    results.append(f"[OK] Python Version: {python_version}")

    results.append(f"[OK] OS: {platform.system()} {platform.release()}")

    required_packages = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn'
    }

    for package_name, display_name in required_packages.items():
        try:
            module = __import__(package_name)
            version = getattr(module, '__version__', 'unknown')
            results.append(f"[OK] {display_name}: {version}")
        except ImportError:
            results.append(f"[ERROR] {display_name}: NOT INSTALLED")

    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

    if in_venv:
        results.append(f"[OK] Virtual Environment: Active ({sys.prefix})")
    else:
        results.append("[WARNING] Virtual Environment: Not active")

    return "\n".join(results)

print("=" * 50)
print("LAB 0: ENVIRONMENT VERIFICATION")
print("=" * 50)
print(verify_environment())
print("=" * 50)