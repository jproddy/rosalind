'''
Finding a Protein Motif
http://rosalind.info/problems/mprt/

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
'''
import regex as re
import urllib3

filename = 'rosalind_mprt.txt'
MOTIF = 'N[^P][ST][^P]'

def find_protein_motif(uniprot_id, http, motif=MOTIF):
	url = f'http://www.uniprot.org/uniprot/{uniprot_id}.fasta'
	response = http.request('GET', url)
	fasta = response.data.decode()
	if not fasta:
		return []
	protein = fasta[fasta.index('\n')+1:].replace('\n', '')
	return [match.start() + 1 for match in re.finditer(motif, protein, overlapped=True)]

def find_protein_motif_list(uniprot_ids):
	urllib3.disable_warnings()
	http = urllib3.PoolManager()
	return {uniprot_id: find_protein_motif(uniprot_id, http) for uniprot_id in uniprot_ids}

def main():
	with open(filename) as f:
		uniprot_ids = [line.strip() for line in f.readlines()]
	motif_matches = find_protein_motif_list(uniprot_ids)
	for uniprot_id, matches in motif_matches.items():
		if matches:
			print(uniprot_id)
			print(' '.join(map(str, matches)))

if __name__ == '__main__':
	main()
