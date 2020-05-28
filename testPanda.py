import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


un_panda = [100, 5, 20, 80]
k = 2

# on initialise le bebe panda avec 0 partout
un_bebe_panda = [0,0,0,0]

# une boucle qui parcourt chacune des 4 mesures
for index in range(4):
    # on divise chaque mesure par le coefficient k
    un_bebe_panda[index] = un_panda[index] / k

famille_panda = [
    [100, 5  , 20, 80], # maman panda
    [50 , 2.5, 10, 40], # bébé panda
    [110, 6  , 22, 80], # papa panda
]
famille_panda_numpy = np.array(famille_panda)

famille_panda_df = pd.DataFrame(famille_panda_numpy,
                                index = ['maman', 'bébé','papa'],
                                columns = ['pattes', 'poils', 'queue', 'ventre'])



for line in famille_panda_df.iterrows():
    index_line = line[0]
    content_line = line[1]
    print("Voici le panda %s :" % index_line)
    print(content_line)
    print("--------------------")