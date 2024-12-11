def create_codon_dict(file_path):
  file = open(path)
  rows = file.readlines()
  file.close()
  milon = {}
  for row in rows :
    row = row.strip().split('\t')
    codon = row[0]
    amino_acids = row[2]
    milon[codon] = amino_acids 
  return milon



