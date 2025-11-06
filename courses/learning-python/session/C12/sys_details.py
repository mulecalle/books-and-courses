import sys

# Imprime plataforma
print(sys.platform, '[Imprime plataforma]')

# Version del sistema
print(sys.version, '[Version del sistema]')

# Directorios donde busca los módulos en el orden en el cual busca
print(sys.path, '[Directorios donde busca los modulos en el orden en el cual busca]')

# los primeros 4 primeros lugares en orden en donde se buscan los módulos de python
print(sys.path[:4], '[Primeros 4 directorios donde busca los modulos en el orden en el cual busca]')

