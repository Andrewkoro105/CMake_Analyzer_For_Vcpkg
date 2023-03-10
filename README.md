# CMake_Analyzer_For_Vcpkg
## EN
### Description
This script parses `CMakeList.txt` and installs all dependencies 
#### Usage
You have to run the script in the folder where `CMakeList.txt` is located, the first argument can be the install command (default: `vcpkg install `, pay attention to the space at the end of the command). After analysis, you will be asked if you want to run the install command list (`[Y/n]` enter `y` - yes or `n` - no. By default, if you leave the input blank, `y` will apply) 
### Analysis
- [x] searching for libraries in `find_package`
- [x] recursively analyze files from `add_subdirectory`
- [ ] add repositories specified with `#/roots for vcpkg:`
---
## Ru
### Описание
Этот скрипт анализирует `CMakeList.txt` и устанавливает все зависимости 
### Использование
Нужно запустить скрипт в папке в которой находится `CMakeList.txt`, первым аргументом можно указать команду установки (по умолчанию: `vcpkg install `, обратите внимание на пробел в конце команды). После анализа вас спросят нужно ли запускать список установочных команд (`[Y/n]` введите `y` - yes или `n` - no. По умолчанию, если оставить ввод пустым, то применится `y`) 
### Анализ
- [x] поиск библиотек в `find_package`
- [x] рекурсивный анализ файлов из `add_subdirectory`
- [ ] добавление репозиториев указанных с помощью `#/pоrts for vcpkg:`
