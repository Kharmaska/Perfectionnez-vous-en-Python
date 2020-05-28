import os
import logging as lg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class SetOfParliamentMembers:
  def __init__(self, name):
    self.name = name
  
  def data_from_csv(self, csv_file):
    self.dataframe = pd.read_csv(csv_file, sept=";")
    
  def data_from_dataframe(self, dataframe):
    self.dataframe = dataframe
    
  def display_chart(self):
        data = self.dataframe
        female_mps = data[data.sexe == "F"]
        male_mps = data[data.sexe == "H"]

        counts = [len(female_mps), len(male_mps)]
        counts = np.array(counts)
        nb_mps = counts.sum()
        proportions = counts / nb_mps

        labels = ["Female ({})".format(counts[0]), "Male ({})".format(counts[1])]

        fig, ax = plt.subplots()
        ax.axis("equal")
        ax.pie(
                proportions,
                labels=labels,
                autopct="%1.1f pourcents"
                )
        plt.title("{} ({} MPs)".format(self.name, nb_mps))
        plt.show()
      
  def split_by_political_party(self):
    result = {}
    data = self.dataframe
    
    all_parties = data["parti_ratt_financier"].dropna().unique()
    
    for party in all_parties:
      data_subset = data[data.parti_ratt_financier == party]
      subset = SetOfParliamentMembers('Mps from party "{}"'.format(party))
      subset.data_from_dataframe(data_subset)
      result[party] = subset
    
    return result
  
   

def launch_analysis(data_file):
  directory = os.path.dirname(os.path.dirname(__file__))
  path_to_file = os.path.join(directory, "data", data_file)
  
  try:
    with open(path_to_file, 'r') as file:
      preview = file.readline()
    lg.debug("Yeah! We managed to read the file. Here is a preview: {}".format(preview))
    
  except FileNotFoundError as e:
    lg.critical('Ow :( The file was not found. Here is the message:{}'.format(e))
  
  

def main():
  launch_analysis('current_mps.csv')
  

if __name__ == "__main__":
  main()