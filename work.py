# import os
# folder = r"C:\Users\user\Desktop\Python"

# for filename in os.listdir(folder):
#     if filename.endswith(".txt"):
#         new_name = "project_" + filename
#         os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
# print("Done")

# import os
# folder = r"C:\Users\user\Desktop\Python"
# prefix = "Demon_Slayer_"

# for filename in os.listdir(folder):
#     full_path = os.path.join(folder, filename)

#     if (
#         os.path.isfile(full_path)
#         and filename.endswith(".txt")
#         and not filename.startswith(prefix)
#     ):
#         new_name = prefix + filename
#         new_path = os.path.join(folder, new_name)

#         os.rename(full_path, new_path)
#         print(f"Renamed: {filename} > {new_name}")
# print("Done")


# import os
# import shutil
# folder = r"C:\Users\user\Desktop\Python"
# prefix = "Demon_Slayer_"
# target_folder = "texts"
# target_path = os.path.join(folder, target_folder)
# os.makedirs(target_path, exist_ok=True)

# for filename in os.listdir(folder):
#     full_path = os.path.join(folder, filename)

#     if (
#         os.path.isfile(full_path)
#         and filename.endswith(".txt")
#         and not filename.startswith(prefix)
#     ):
#         new_name = prefix + filename
#         new_path = os.path.join(target_path, new_name)
#         shutil.move(full_path, new_path)
#         print(f"Moved & Renamed: {filename} > {new_name} (to {target_folder}/)")

# print(f"Done. Files moved to: {target_path}")



from bs4 import BeautifulSoup
import os

folder = r"C:\Users\user\Desktop\site_files"

translated_folder = os.path.join(folder, "translated")
os.makedirs(translated_folder, exist_ok=True)

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome Page</title>
</head>
<body>
    <header>
        <h1>Welcome to Demon Slayer Fansite</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="characters.html">Characters</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>About the Series</h2>
            <p>Demon Slayer is a popular anime and manga series.</p>
            <p>Follow Tanjiro and his friends on their adventures!</p>
        </section>

        <section>
            <h2>Latest News</h2>
            <p>New episodes release every Sunday.</p>
            <button>Subscribe</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Demon Slayer Fansite</p>
    </footer>
</body>
</html>'''

file_path = os.path.join(folder, "index.html")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Файл создан: {file_path}")


translations = {
    "Welcome to Demon Slayer Fansite":
    "Добро Пожаловать в Фансайт по Клинку, Рассекающего Демонов",
    "Home":
    "Главная",
    "Characters":
    "Персонажи",
    "Contact":
    "Связаться",
    "About the Series":
    "О Сериях",
    "Demon Slayer is a popular anime and manga series.":
    "Клинок, Рассекающий Демонов - это популярная серия аниме и манги.",
    "Follow Tanjiro and his friends on their adventures!":
    "Следуйте за Танджиро и его друзьями на их приключения!",
    "Latest News":
    "Последние Новости",
    "New episodes release every Sunday.":
    "Новые Эпизоды выходят каждое Воскресенье.",
    "Subscribe":
    "Подписаться"
}

log_path = os.path.join(translated_folder, "log.txt")
with open(log_path, "w", encoding="utf-8") as log:
    log.write("Лог перевода HTML файлов\n\n")

for filename in os.listdir(folder):
    if filename.endswith(".html"):
        file_path = os.path.join(folder, filename)


        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

            tags = soup.find_all(["h1", "li", "h2", "p", "button"])
            translated_count = 0

            for tag in tags:
                original = tag.get_text().strip()
                if original in translations:
                    tag.string = translations[original]
                    translated_count += 1

            new_file_path = os.path.join(translated_folder, filename)
            with open(new_file_path, "w", encoding="utf-8") as f:
                f.write(str(soup))

                with open(log_path, "a", encoding="utf-8") as log:
                    log.write(f"{filename}: переведены {translated_count} элементов\n")

print(f"Все файлы переведены и сохранены в {translated_folder}")