#Please write a program to compress and decompress the string "hello world!hello
#world!hello world!hello world!".

import zlib
import sys

class string_compressor:
    def __init__(self, input_string:str):
        self.input_sentence:str =input_string

    def compress_string(self,)->str:
        sentence_bytes =self.input_sentence.encode('utf-8')
        compressed_sentence=zlib.compress(sentence_bytes)
        return compressed_sentence
    
    def decompress_string(self,)->str:
        compressed_string=self.compress_string()
        decompress_sentence=zlib.decompress(compressed_string)
        original_sentence = decompress_sentence.decode('utf-8')
        return original_sentence
    
if __name__=="__main__":
    input_string="hello world!hello world!hello world!hello world!"
    compressor=string_compressor(input_string)
    compressed_data=compressor.compress_string()
    decompressed_data=compressor.decompress_string()
    print(f"Original String: {input_string} with size {sys.getsizeof(input_string)} bytes")
    print(f"Compressed String: {compressed_data} with size {sys.getsizeof(compressed_data)} bytes")
    print(f"Decompressed String: {decompressed_data} with size {sys.getsizeof(decompressed_data)} bytes")