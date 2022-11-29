import synonyms as syn
def test_cosine_similarity(self):
    self.assertAlmostEqual(syn.cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}), 0.7, places = 2)


def test_build_semantic_descriptors(self):
    sentences = [["i", "am", "a", "sick", "man"],
    ["i", "am", "a", "spiteful", "man"],
    ["i", "am", "an", "unattractive", "man"],
    ["i", "believe", "my", "liver", "is", "diseased"],
    ["however", "i", "know", "nothing", "at", "all", "about", "my",
    "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    sem_desc = syn.build_semantic_descriptors(sentences)
    self.assertEqual(sem_desc["man"], {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1})

    self.assertEqual(sem_desc["liver"], {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1})


def test_build_semantic_descriptors_from_files(self):
    f1 = open("text1.txt", "w")
    f2 = open("text2.txt", "w")
    f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\n")
    f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
    f1.close()
    f2.clos
    sem_desc = syn.build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])
    self.assertEqual(sem_desc["man"], {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,
"unattractive": 1})
    self.assertEqual(sem_desc["liver"], {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased":1})
    self.assertEqual(sem_desc["nothing"]["ails"], 1)

# @weight(1)
# @visibility("visible")
def test_most_similar_word(self):
    sem_desc = {"dog": {"cat": 1, "food": 1},"cat": {"dog": 1}}
    self.assertEqual(syn.most_similar_word("dog", ["cat", "rat"], sem_desc, syn.cosine_similarity), "cat")


def test_run_similarity_test(self):
    f1 = open("text1.txt", "w")
    f2 = open("text2.txt", "w")
    f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased\n")
    f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
    f1.close()
    f2.clo

    f3 = open("test.txt", "w")
    f3.write("man i liver i\nsick man certain man")
    f3.close()
    sem_desc = syn.build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])
    res = syn.run_similarity_test("test.txt", sem_desc, syn.cosine_similarity)
    self.assertEqual(res, 100.0)

test_cosine_similarity(self)
