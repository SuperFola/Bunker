from ..window import Window

# pour ajouter une app :
# from .fichier import nom_de_l'app
# puis on l'ajoute à la liste des apps

app_list = []

from .test import App
app_list.append(App)

from .process import ProcessManagerWindow
app_list.append(ProcessManagerWindow)
