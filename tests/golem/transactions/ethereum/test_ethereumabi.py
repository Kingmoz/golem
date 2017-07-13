import unittest

from eth_utils import encode_hex
from ethereum.abi import encode_abi


class TestEthereumAbi(unittest.TestCase):

    def testEncodeAbi(self):
        enc = encode_hex(encode_abi(
            ['uint32', 'uint32[]', 'bytes10', 'bytes'],
            [int(0x123), [int(0x456), int(0x789)],
             "1234567890", "Hello, world!"]
        ))
        data = "0000000000000000000000000000000000000000000000000000000000000" \
               "1230000000000000000000000000000000000000000000000000000000000" \
               "0000803132333435363738393000000000000000000000000000000000000" \
               "0000000000000000000000000000000000000000000000000000000000000" \
               "0000000000e00000000000000000000000000000000000000000000000000" \
               "0000000000000020000000000000000000000000000000000000000000000" \
               "0000000000000004560000000000000000000000000000000000000000000" \
               "0000000000000000007890000000000000000000000000000000000000000" \
               "00000000000000000000000d48656c6c6f2c20776f726c642100000000000" \
               "000000000000000000000000000"
        self.assertEqual(enc, '0x' + data)

    def testAddress(self):
        addr = '407d73d8a49eeb85d32cf465507dd71d507100c1'
        enc = encode_hex(encode_abi(
            ['address'],
            ['407d73d8a49eeb85d32cf465507dd71d507100c1']
        ))
        self.assertEqual(enc[-40:], addr)
