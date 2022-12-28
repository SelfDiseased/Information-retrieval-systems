import unittest
import forward_index
import inverted_index

class IndexesTests(unittest.TestCase):
  def setUp(self):
    self.forwardIndex = forward_index.createDictionary()[0]
    self.invertedIndex = inverted_index.createDictionary()[0]

  def test_forward_index(self):
    self.assertEqual(self.forwardIndex.get('file1.txt'), ['software', 'helping', 'work'])
    self.assertEqual(self.forwardIndex.get('file2.txt'), ['over'])
    self.assertEqual(self.forwardIndex.get('file3.txt'), ['software', 'over'])
    self.assertEqual(self.forwardIndex.get('file4.txt'), ['collaboration', 'over', 'negotiation'])
    self.assertEqual(self.forwardIndex.get('file5.txt'), ['over'])

  def test_inverted_index(self):
    self.assertEqual(self.invertedIndex.get('over'), ['file2.txt', 'file3.txt', 'file4.txt', 'file5.txt'])
    self.assertEqual(self.invertedIndex.get('software'), ['file1.txt', 'file3.txt'])
    self.assertEqual(self.invertedIndex.get('processes'), ['file2.txt'])
    self.assertEqual(self.invertedIndex.get('collaboration'), ['file4.txt'])
    self.assertEqual(self.invertedIndex.get('and'), ['file1.txt', 'file2.txt'])

if __name__ == "__main__":
  unittest.main()