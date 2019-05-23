"""
Compressing data with self created class
Using genetic coding as example
Creating a wrapper for int to bit string simplification

"""
from typing import Generic, TypeVar
T = TypeVar("T")

class Int(Generic[T]):

	def __init__(self, meth):
		self.m = method

	def __call__(self, meth):
		def wrapper(gene_instance):
			met = gene_instance(original)
			bit_int = met.bitstring

class CompressedGene:
	def __init__(self, original):
		self._compress(original)

	def _compress(self, original):
		self.bit_string = 1
		for nucleotide in original.upper():
			self.bit_string <<= 2
			if nucleotide == "A":
				self.bit_string |= 0b00
			elif nucleotide == "C":
				self.bit_string |= 0b01
			elif nucleotide == "G":
				self.bit_string |= 0b10
			elif nucleotide == "T":
				self.bit_string |= 0b11
			else:
				raise ValueError("Invalid nucleotide: {}".format(nucleotide))

	def decompress(self):
		gene = ""
		for i in range(0, self.bit_string.bit_length() - 1, 2):
			bits = self.bit_string >> i & 0b11
			if bits == 0b00:
				gene += "A"
			elif bits == 0b01:
				gene += "C"
			elif bits == 0b10:
				gene += "G"
			elif bits == 0b11:
				gene += "T"
			else:
				raise ValueError("Invalid bits: {}".format(bits))

		return gene[::-1]

	def __str__(self):
		return self.decompress()


if __name__ == '__main__':
	from sys import getsizeof
	original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
	compressed = CompressedGene(original)
	print("Original byte size: {}".format(getsizeof(original)))
	print("Compressed byte size: {}".format(getsizeof(compressed.bit_string)))
	print(compressed)
	print("Original and decompressed is same: {}".format(original == compressed.decompress()))
