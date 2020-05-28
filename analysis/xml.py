import os

def launch_analysis(data_file):
  directory = os.path.dirname(os.path.dirname(__file__))
  path_to_file = os.path.join(directory, "data", data_file)
  with open(path_to_file, 'r') as file:
    preview = file.readline()
  
  print("Yeah! We managed to read the file. Here is a preview: {}".format(preview))

def main():
  launch_analysis('CRSANR5L15S2017E1N001.xml')
  

if __name__ == "__main__":
  main()