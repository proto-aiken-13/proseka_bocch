import os

structure = {
    "parsers": ["__init__.py", "time_parser.py", "command_parser.py"],
    "models": ["__init__.py", "task.py", "token_wallet.py"],
}

base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"📂 Creating structure in: {base_dir}\n")

for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"✅ Created folder: {folder_path}")

    for file in files:
        file_path = os.path.join(folder_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                if file == "__init__.py":
                    f.write(f"# Init for {folder}\n")
                else:
                    f.write(f"# {file.split('.')[0].capitalize()} module\n")
            print(f"  📝 Created file: {file_path}")
        else:
            print(f"  ⚠️ Skipped existing file: {file_path}")

print("\n🎉 Project folders and files initialized successfully.")
