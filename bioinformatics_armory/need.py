'''
Pairwise Global Alignment

http://rosalind.info/problems/need/

Given: Two GenBank IDs.

Return: The maximum global alignment score between the DNA strings associated with these IDs.
'''

'''
from Bio.Emboss.Applications import NeedleCommandline

Wasn't able to get the command line tool easily installed but the above
import should presumably work with a valid install?

Instead, after coping the relevant DNA strings from:
	https://www.ncbi.nlm.nih.gov/genbank/sequenceids/

Used the online tool at:
	https://www.ebi.ac.uk/Tools/psa/emboss_needle/

With the following settings:
	OUTPUT FORMAT :		pair
	MATRIX:				DNAfull
	GAP OPEN:			10
	GAP EXTEND:			1.0
	END GAP PENALTY:	true
	END GAP OPEN:		10
	END GAP EXTEND:		1.0
'''

pass
